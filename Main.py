import streamlit as st

st.title("좋아하는 과목")
st.header("디자인 :pencil:")

st.write("---")

st.title("이름/학번")
name = st.text_input('이름을 입력')
id = st.text_input('학번을 입력')

if st.button('저장'):
    if 'name' not in st.session_state:
        st.session_state['name'] = name