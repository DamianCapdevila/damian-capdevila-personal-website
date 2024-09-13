import openai
import os
import copy
from utilities import file_handler

OPENAI_API_KEY = os.getenv('ApiKey')
openai.api_key = OPENAI_API_KEY
openai.version = 'gpt-4o-2024-08-06'  

cv_content = file_handler.load_cvs_from_folder(file_handler.assets_folder_path)
SYSTEM_MESSAGE = f"""
        You are an AI chatbot that provides responses based on the following CVs:
        {cv_content}

        If the user requests contact information, answer based on the following information:
        Linkedin: https://linkedin.com/in/damiancapdevila
        Phone number: +34 673 47 82 70
        Email address: damian.capdevila@hotmail.com
        Blog: https://substack.com/home/post/p-144238956?r=3cvmsg&utm_campaign=post&utm_medium=web
        GitHub: https://github.com/damiancapdevila

        Additionally, tell the user that Damian has the legal right to work in every EU country and also in Argentina.

        Also, if the user asks for services provided by Damian, answer based on the following:
        Damian Capdevila provides consultancy services for transitioning into software development, Resume and Linkedin profile review and
        enhancements, international relocation advice, and interview preparation. 
        Point the user to Damian's contact information.
        """

# Function to get a response from GPT-4o based on Damian CVs. We consider the last 10 messages for context.
def get_gpt4o_response(messages):
    try:
        predefinedSystemMessage = {"role": "system", "content": SYSTEM_MESSAGE}
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
