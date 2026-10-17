import streamlit as st


def footer_home():
    st.markdown("""
        <div style="margin-top:0.5rem; display:flex; gap:6px; justify-content:center; align-items:center">
            <p style="font-size:25px; color:#003B5C; font-weight:bold; margin:0;">
            Created by Team SnapClass <span style="color:#E5484D;">&hearts;</span></p>
        </div>

    """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown("""
        <div style="margin-top: 2rem; display:flex; gap:6px; justify-content:center; align-items:center">
            <p style="font-size:25px; color:#4A6B82; margin:0;">
            Created by Team SnapClass <span style="color:#E5484D;">&hearts;</span></p>
        </div>
        
    """, unsafe_allow_html=True)