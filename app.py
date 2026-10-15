import streamlit as st
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen
from src.screens.home_screen import home_screen
from src.components.dialog_auto_enroll import auto_enroll_dialog


def main():
    st.set_page_config(page_title='SnapClass - Making Attendance Faster using AI', page_icon='https://th.bing.com/th/id/OIP.crawWkupQuJ15cyfjI5U0gHaHa?w=168&h=180&c=7&r=0&o=7&dpr=2&pid=1.7&rm=3')

    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()

        case 'student':
            student_screen()

        case None:
            home_screen()

    join_code=st.query_params.get('join-code')
    if join_code:
        if st.session_state.login_type != 'student':
            st.session_state.login_type = 'student'
            st.rerun()
        if st.session_sate.get('is_logged_in') and st.session_sate.get('user_roles') == 'student':
            auto_enroll_dialog(join_code)

main()
