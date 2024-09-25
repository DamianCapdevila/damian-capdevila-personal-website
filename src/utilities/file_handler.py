import os
import pdfplumber
import requests
from io import BytesIO
import logging

# Load CV content from multiple PDF files in the "assets" folder
def load_cvs_from_secure_location():
    combined_text = ""
    cv_urls = [
        os.getenv('CV_PRESALES_URL'),
        os.getenv('CV_SOFTWARE_URL')
    ]
    for url in cv_urls:
        try:
            combined_text += load_cv_from_url(url) + "\n\n"
        except Exception as e:
            logging.error(f"Error loading CV from {url}: {str(e)}")
    return combined_text

def load_cv_from_url(url):
    file_id = url.split('/d/')[1].split('/')[0]
    download_url = f"https://drive.google.com/uc?export=download&id={file_id}"
    response = requests.get(download_url)
    pdf_content = BytesIO(response.content)
    
    text = ""
    with pdfplumber.open(pdf_content) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

# Remove the assets_folder_path variable as it's no longer needed