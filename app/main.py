# run_app.py
import os
import socket
import sys
from dotenv import load_dotenv
from pyngrok import ngrok

def find_available_ports(start=8501, end=8510):
    """
    Finds available ports within a specified range.
    Returns a list of free ports.
    """
    available_ports = []
    for port in range(start, end + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            if sock.connect_ex(("localhost", port)) != 0:
                available_ports.append(port)
    return available_ports

def run_streamlit_app():
    """
    1. Loads environment variables (ngrok token).
    2. Finds a free port for Streamlit.
    3. Opens an ngrok tunnel to that port.
    4. Runs Streamlit on that port with `os.system(...)`.
    """
    # Load tokens and environment variables
    load_dotenv()  
    ngrok_api_token = os.getenv('NGROK_AUTH_TOKEN')
    if not ngrok_api_token:
        print("NGROK_AUTH_TOKEN is not set in .env. Exiting...")
        sys.exit(1)

    # Set ngrok auth token
    ngrok.set_auth_token(ngrok_api_token)
    
    # Find the first free port
    ports_list = find_available_ports()
    if not ports_list:
        print("No free ports available within 8501..8510!")
        sys.exit(1)
    selected_port = ports_list[0]
    print(f"Selected port: {selected_port}")

    # Create an ngrok tunnel to that port
    public_url = ngrok.connect(addr=selected_port, proto='http', bind_tls=True)
    print(f"Public URL: {public_url.public_url}")

    # Suppress Streamlit's frontend warnings by passing logger.level=error
    streamlit_cmd = f"streamlit run app.py --server.port={selected_port} --logger.level=error --server.headless=true"
    print(f"Running command: {streamlit_cmd}\n")
    
    # Run the  Streamlit app in the background.
    os.system(streamlit_cmd)

    # Close tunnels after exiting application
    tunnels = ngrok.get_tunnels()
    for tunnel in tunnels:
        print(f"Shutting down tunnel: {tunnel.public_url} -> {tunnel.config['addr']}")
        ngrok.disconnect(tunnel.public_url)

if __name__ == "__main__":
    run_streamlit_app()
