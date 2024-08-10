from forms.contact import contact_form
from utilities.gpt_communication import get_gpt4o_response
import streamlit as st


st.title("💬 Ask anything about me!")
st.caption("🚀 I know Damian Capdevila very well. Feel free to ask anything about him!")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder="Tell me something about Damian Capdevila"):
    full_response = ""
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = get_gpt4o_response(st.session_state.messages)
    msg = response
    with st.chat_message("assistant"):
        full_response = st.write_stream(msg)
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Call to Action - Contact Me
st.write("---")
st.subheader("📩 Let's Talk!")
st.write("If you have any questions or want to work together, feel free to reach out!")
if st.button("Contact Me"):
    contact_form()


