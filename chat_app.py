import streamlit as st

st.title("情感陪伴agent") #设置页面标题

#agent的API调用
import requests
def call_agent(input:str):
    url='http://106.55.142.84:8000/Call/'
    headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
} #请求头
    data = {
        "input": input
    } #请求体
    response = requests.post(url, headers=headers, json=data)
    response = response.json()
    return response["content"]


#初始化历史消息
if "messages" not in st.session_state:
    st.session_state.messages = []

#应用重新运行时，显示历史聊天记录
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("宝宝，想和我说什么呀？"):
    # 将用户消息添加到聊天记录中
    st.session_state.messages.append({"role": "user", "content": prompt})
    # 用消息容器显示用户消息
    with st.chat_message("user"):
        st.write(prompt)
    #用消息容器显示agent响应
    with st.chat_message("assistant"):
        stream = call_agent(prompt)
        response = st.write(stream)
    st.session_state.messages.append({"role": "assistant", "content": stream})