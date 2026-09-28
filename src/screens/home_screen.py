import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home
def home_screen():


    header_home()
    style_background_home()
    style_base_layout()


    col1, col2 = st.columns(2)

    with col1:
        st.header("I'm Student")
        st.image("Student.png", width=145)
        if st.button('Student Portal', type='primary'):
            st.session_state['login_type']='student'
            st.rerun()
 
    with col2:
        st.header("I'm Teacher")
        st.image("Teacher.png", width=145)
        if st.button('Teacher Portal', type='primary'):
            st.session_state['login_type']='teacher'
            st.rerun()
    footer_home()