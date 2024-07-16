import streamlit as st

st.header('문제 1')
quiz = st.radio(
    "1+1",
    ["0", "1", "2","3","4"])

st.write('---')

st.header('문제 2')
st.write('5월 8일은 무슨날?')
quiz2 = st.text_input('답을 입력')

if "answer" not in st.session_state:
    st.session_state.answer = "답안을 제출"
if "answer2" not in st.session_state:
    st.session_state.answer2 = "답안을 제출"

if st.button('제출'):
    if quiz2 == '어버이날'or'어버이 날':
        st.session_state.answer2 = "정답"
    else:
        st.session_state.answer = "오답"
    if quiz == "2":
        st.session_state.answer = "정답"
    else:
        st.session_state.answer = "오답"
   