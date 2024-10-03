from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
import streamlit as st
from streamlit_chat import message

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv(), override=True)

st.set_page_config(
    page_title="Assistant",
    page_icon="🤖"    # press windows and dot for  emojis
)

st.subheader("Your Custom coding Assistant")

chat = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
)

if 'messages' not in st.session_state:
    st.session_state.messages=[]

with st.sidebar:
    system_message = st.text_input(label="Assistant Role")
    user_prompt = st.text_input(label="Please enter your prompt")
    if system_message:
        if not any(isinstance(x, SystemMessage) for x in st.session_state.messages):
            st.session_state.messages.append(SystemMessage(content=system_message))
        
    if user_prompt:
        st.session_state.messages.append(HumanMessage(content = user_prompt))
        
        with st.spinner("Thinking....."):
            response = chat(st.session_state.messages)
        
        st.session_state.messages.append(AIMessage(content=response.content))

#st.session_state.messages
#message("This is a user",  is_user=True)
#message("This is chatgpt", is_user=False)

for i, msg, in enumerate(st.session_state.messages[1:]):
    if i%2==0:
        message(msg.content, is_user=True, key=f"{i}+😎")
    else:
        message(msg.content, is_user=False, key=f"{i}+😍")    

#-------------------------------------------------
#prompt bar to be places at the center
#llm streaming remove spin