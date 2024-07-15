import streamlit as st

quiz = st.radio(
    "1+1",
    ["0", "1", "2","3","4"])
if st.button('제출'):
    if quiz == "2":
        if "answer" not in st.session_state:
            st.session_state.answer = "정답"
        else:
            st.session_state.answer = "정답"
    else:
        if "answer" not in st.session_state:
            st.session_state.answer = "오답"
        else:
            st.session_state.answer = "오답"

   