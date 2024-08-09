from forms.contact import contact_form
import streamlit as st
import openai
import pdfplumber
import os

OPENAI_API_KEY = os.getenv('ApiKey')
# Set up OpenAI API key
openai.api_key = OPENAI_API_KEY  

# Load CV content from multiple PDF files in the "assets" folder
def load_cvs_from_folder(folder_path):
    combined_text = ""
    for cv_file in ["Damian Capdevila - Presales Engineer - 2024.pdf", "Damian Capdevila - Software Engineer - 2024.pdf"]:  # Replace with actual file names if different
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

# Load all CVs from the "assets" folder
cv_content = load_cvs_from_folder(assets_folder_path)

# Function to get a response from GPT-4 Turbo based on CVs
def get_gpt4o_response(user_input, cv_content):
    try:
        prompt = f"""
        You are an AI chatbot that provides responses based on the following CVs:
        {cv_content}
        """
        response = openai.chat.completions.create(
             model="gpt-4o",  # Using GPT-4o
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": user_input}
            ],
            max_tokens=1500,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"

st.title("💬 Ask anything about me")
st.caption("🚀I am a Streamlit chatbot powered by OpenAI. I know Damian quite well. Feel free to ask anything about Damian!")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder="Give me a summary about Damian Capdevila"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = get_gpt4o_response(prompt, cv_content)
    msg = response
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)

# Call to Action - Contact Me
st.write("---")
st.subheader("📩 Let's Talk!")
st.write("If you have any questions or want to work together, feel free to reach out!")
if st.button("Contact Me"):
    contact_form()


