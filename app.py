import streamlit as st
import openai
from streamlit_chat import message
openai.api_key = 'YOUR_API_KEY'

def api_calling(prompt):
    completions = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": prompt}], 
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].message['content'] 
    return message

st.title("ChatGPT ChatBot With Streamlit and OpenAI")
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = []

if 'openai_response' not in st.session_state:
    st.session_state['openai_response'] = []

def get_text():
    input_text = st.text_input("write here", key="input")
    return input_text

user_input = get_text()

if user_input:
    output = api_calling(user_input)
    output = output.lstrip("\n")

    st.session_state.openai_response.append(user_input)
    st.session_state.user_input.append(output)

message_history = st.empty()

if st.session_state['user_input']:
    for i in range(len(st.session_state['user_input']) - 1, -1, -1):
        message(st.session_state["user_input"][i], key=str(i), avatar_style="icons")
        message(st.session_state['openai_response'][i], avatar_style="miniavs", is_user=True, key=str(i) + 'data_by_user')