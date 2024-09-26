import openai
import os
import copy
from utilities import file_handler
import logging
import threading

OPENAI_API_KEY = os.getenv('ApiKey')
openai.api_key = OPENAI_API_KEY
openai.version = 'gpt-4o-2024-08-06'  

cv_content = "CV content is being loaded..."
cv_loading_complete = threading.Event()

def load_cvs_background():
    global cv_content
    try:
        cv_content = file_handler.load_cvs_from_secure_location()
        if not cv_content:
            cv_content = "CV content unavailable."
    except Exception as e:
        logging.error(f"Error loading CVs: {str(e)}")
        cv_content = "Error loading CV content."
    finally:
        cv_loading_complete.set()

# Start loading CVs in the background
threading.Thread(target=load_cvs_background, daemon=True).start()

SYSTEM_MESSAGE = """
        You are an AI chatbot that provides responses about Damian Capdevila based on the following CVs:
        {{cv_content}}

        If the user requests contact information, answer based on the following information:
        
        Linkedin: https://linkedin.com/in/damiancapdevila
        Email address: contact@damian-capdevila.com
        Blog: https://substack.com/home/post/p-144238956?r=3cvmsg&utm_campaign=post&utm_medium=web
        GitHub: https://github.com/damiancapdevila

        Damian has the legal right to work in every EU country and also in Argentina.

        If the user asks for services provided by Damian, answer based on the following:
        
        Damian Capdevila provides consultancy services for transitioning into software development, Resume and Linkedin profile review and
        enhancements, international relocation advice, and interview preparation. 
        Point the user to Damian's contact information.
        """

def get_gpt4o_response(messages):
    try:
        global cv_content
        if not cv_loading_complete.is_set():
            cv_loading_complete.wait(timeout=10)  # Wait for up to 10 seconds for CV loading
        
        system_message_with_cv = SYSTEM_MESSAGE.replace("{{cv_content}}", cv_content)
        predefinedSystemMessage = {"role": "system", "content": system_message_with_cv}
        modifiedMessages = copy.deepcopy(messages)
        modifiedMessages.insert(len(messages) - 1, predefinedSystemMessage)
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=modifiedMessages[-10:],
            max_tokens=1500,
            temperature=0.7,
            stream=True 
        )
        return response
    except Exception as e:
        return str(e)
