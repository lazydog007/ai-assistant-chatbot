import os
import re
from dotenv import load_dotenv
from openai import OpenAI
import openai
import streamlit as st

from assistant import generate_response

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_ASSISTANT_ID = os.getenv("OPENAI_ASSISTANT_ID")
client = openai.OpenAI(api_key=OPENAI_API_KEY)
assistant = client.beta.assistants.retrieve(OPENAI_ASSISTANT_ID)

st.set_page_config(
    page_title="Fuerza Gym Support",
    page_icon=":muscle:",
)

st.title("Fuerza Gym Customer Support")

if "assistant" not in st.session_state:
    st.session_state["assistant"] = assistant

if "messages_assistant" not in st.session_state:
    st.session_state.messages_assistant = []

for message in st.session_state.messages_assistant:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What's up?"):
    if len(st.session_state.messages_assistant) < 10:  # Considering both user and assistant messages
        st.session_state.messages_assistant.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            user_id = "123" # TODO: This is what you need to change to keep track of convos
            message = generate_response(prompt, user_id)
            print('\n')
            print(message)
            print('\n')
            cleaned_messaged = re.sub(r"【.*?】", "", message)
            print('\n')
            print(cleaned_messaged)
            print('\n')
            st.markdown(cleaned_messaged)
        st.session_state.messages_assistant.append({"role": "assistant", "content": cleaned_messaged})
    else:
        st.error("You have reached the maximum amount of messages")