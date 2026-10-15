import streamlit as st


def footer_home():
    st.markdown("""
        <div style="margin-top:0.5rem; display:flex; gap:6px; justify-content:center; align-items:center">
            <p style="font-size:25px; color:#5B3A70; font-weight:bold; margin:0;">
            Created with <span style="color:#D81B60;">&hearts;</p>
        </div>

    """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown("""
        <div style="margin-top: 2rem; display:flex; gap:6px; justify-content:center; align-items:center">
            <p style="ont-size:25px; color:#5B3A70; font-weight:bold;>
            Created with <span style="color:#D81B60;">&hearts;</p>
        </div>
        
    """, unsafe_allow_html=True)
