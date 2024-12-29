# Brain-Tumor-Classification

A Python-based project for brain tumor classification and generating medical explanations using LLMs.

## Features
- **Brain Tumor Classification**: Classifies MRI scans as Glioma, Meningioma, No Tumor, or Pituitary using CNN models.
- **Saliency Maps**: Visualizes regions of interest in MRI scans that influence the model's predictions.
- **LLM Explanations**: Generates explanations of the saliency maps using Hugging Face and Google Gemini APIs.

## Project Structure
Brain-Tumor-LLM-Explanations/ 
├── app/│ 
        ├── app.py # Streamlit code │ 
        ├── main.py # Main application logic │ 
        ├── saliency_maps/                      # Directory for saliency maps (ignored in Git) 
├── models/                                     # Pretrained models and weights 
├── notebooks/                                  # Jupyter notebooks for experimentation 
├── .streamlit/                                 # Streamlit configuration files (ignored in Git)
├── .venv/                                      # Virtual environment (ignored in Git)
├── .gitignore
├── .env                                        # Environment Variables (ignored in Git)
├── .gitignore                                  # Gitignore configuration files
├── README.md
├── requirements.txt                            # Package requirements to be installed


## Setup Instructions
### Prerequisites
- Python 3.9+
- Virtual environment tool (e.g., `venv`)
- Create an ngrok account and API key for authentication
- Create a Groq account and API key for authentication
- Create a Google AI studio account and API key for authentication

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Zubin-glitch/Brain-Tumor-Classification.git
   

2. Create and activate a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate

3. Install dependencies:
    ```bash
    pip install -r requirements.txt



### Usage:

- Open the notebooks, run the cells (customize code if needed) and create the CNN models.

- Save the model weights and models itself in your preferred directory. They would be save as .h5 files.

- Run the application:
    ```bash
    cd Brain_Tumor_Classification_Project
    cd app
    python main.py
- In terminal window you should see something like this (The public URL will be different):
    ```bash
    Selected port: 8501
    Public URL: https://c72d-198-244-107-35.ngrok-free.app

- Running command: streamlit run app.py --server.port=8501 --logger.level=error --server.headless=true 

- Simply click on the public url and it should open on your browser.

- Here you can upload an image of an MRI scan from your device and continue from thereon to see the results.

- You can watch a demo of the application run on my LinkedIn page at: https://www.linkedin.com/in/zubin-tobias/

