import streamlit as st
from openai import OpenAI
client = OpenAI(api_key='api_key_here')

st.title("Chat with GPT-5.2")

if 'messages' not in st.session_state:
    st.session_state.messages = [] 
for message in st.session_state.messages:
    st.chat_message(message["role"]).markdown(message["content"])


prompt = st.chat_input("Enter your message:")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message('user').markdown(prompt)

    completion = client.chat.completions.create(
        model="gpt-5.2",
        messages=st.session_state.messages
  
    )
    reply_content = completion.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply_content})
    st.chat_message('assistant').markdown(reply_content)