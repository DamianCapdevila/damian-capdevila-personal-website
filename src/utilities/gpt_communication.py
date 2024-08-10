import openai
import os
import copy
from utilities import file_handler

OPENAI_API_KEY = os.getenv('ApiKey')
openai.api_key = OPENAI_API_KEY  

# Load CVs from the "assets" folder
cv_content = file_handler.load_cvs_from_folder(file_handler.assets_folder_path)
SYSTEM_MESSAGE = f"""
        You are an AI chatbot that provides responses based on the following CVs:
        {cv_content}
        """

# Function to get a response from GPT-4o based on Damian CVs. We consider the last 10 messages for context.
def get_gpt4o_response(messages):
    try:
        predefinedSystemMessage = {"role": "system", "content": SYSTEM_MESSAGE}
        modifiedMessages = copy.deepcopy(messages)
        modifiedMessages.insert(len(messages) - 1, predefinedSystemMessage)
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=modifiedMessages[-10:],
            max_tokens=1500,
            temperature=0.7,
            stream=True 
        )
        return response
    except Exception as e:
        return str(e)
