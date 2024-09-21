from utilities.gpt_communication import get_gpt4o_response
import utilities.helper
import streamlit as st
from assets.chat_resources import *

st.title(CHAT_TITLE)
st.caption(CHAT_CAPTION)
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": INITIAL_ASSISTANT_MESSAGE}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Count the number of user messages
user_message_count = sum(1 for msg in st.session_state.messages if msg["role"] == "user")

if user_message_count < MAX_USER_MESSAGES:
    if prompt := st.chat_input(placeholder=PROMPT_PLACEHOLDER):
        if len(prompt) > MAX_MESSAGE_LENGTH:
            st.warning(MESSAGE_TOO_LONG_WARNING.format(MAX_MESSAGE_LENGTH))
        else:
            full_response = ""
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)
            response = get_gpt4o_response(st.session_state.messages)
            msg = response
            with st.chat_message("assistant"):
                full_response = st.write_stream(msg)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
else:
    st.warning(MAX_USER_MESSAGES_WARNING)

if len(st.session_state.messages) > 2:

    utilities.helper.call_to_action()



