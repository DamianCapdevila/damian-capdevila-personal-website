import os
import pdfplumber

# Load CV content from multiple PDF files in the "assets" folder
def load_cvs_from_folder(folder_path):
    combined_text = ""
    for cv_file in ["Damian Capdevila - Presales Engineer - 2024.pdf", "Damian Capdevila - Software Engineer - 2024.pdf"]:
        file_path = os.path.join(folder_path, cv_file)
        combined_text += load_cv_from_pdf(file_path) + "\n\n"  # Separate each CV's content
    return combined_text

# Load CV content from a single PDF file using pdfplumber
def load_cv_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Adjust the path to the assets folder
assets_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets')