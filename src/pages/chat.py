from forms.contact import contact_form
from utilities.gpt_communication import get_gpt4o_response
import streamlit as st

MAX_MESSAGE_LENGTH = 200  

st.title("💬 Ask anything about Damian!")
st.caption("👂Psst... Did you know that Damian is providing services?")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder="What services does Damian provide?"):
    if len(prompt) > MAX_MESSAGE_LENGTH:
        st.warning(f"Your message is too long. Please limit your message to {MAX_MESSAGE_LENGTH} characters.")
    else:
        full_response = ""
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        response = get_gpt4o_response(st.session_state.messages)
        msg = response
        with st.chat_message("assistant"):
            full_response = st.write_stream(msg)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

if len(st.session_state.messages) > 2:
    # Call to Action - Contact Me 
    st.write("---")
    st.subheader("📩 Let's Talk")
    st.write("If you have any questions or want to work together, feel free to reach out!")
    if st.button("Contact Me"):
        contact_form()



