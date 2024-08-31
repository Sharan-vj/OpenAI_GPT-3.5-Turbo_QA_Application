# Import Dependencies
import streamlit as st
from langchain_openai import OpenAI

# Application Header
st.set_page_config(page_title='QA Application', page_icon=":robot_face:")
st.header(body='Question Answering Application using OpenAI GPT-3.5')


# Get Question Func
def get_question():
    input_text = st.text_input(label='Ask your question')
    return input_text


# Get Response Func
def load_response(question):
    llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0)
    response = llm.invoke(question)
    return response


question = get_question()
response = load_response(question)

submit = st.button('Get Answer')

if submit:
    st.subheader(body="Answer:")
    st.write(response)
