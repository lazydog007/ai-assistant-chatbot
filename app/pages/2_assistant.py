import os
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

st.title("Assistant")

if "assistant" not in st.session_state:
    st.session_state["assistant"] = assistant

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        user_id = "123" # TODO: This is what you need to change to keep track of convos
        message = generate_response(prompt, user_id)
        st.markdown(message)
    st.session_state.messages.append({"role": "assistant", "content": message})