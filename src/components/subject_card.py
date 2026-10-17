import streamlit as st


def subject_card(name, code, section, stats, footer_callback):
    html = f"""
        <div style="background:white; border-left: 8px solid #0077BE; padding:25px; border-radius: 20px; border: 1px solid #CFE6F5; margin-bottom: 20px;">
        <h3 style="margin:0; color: #003B5C; font-size: 1.5rem">{name}</h3>
        <p style="color:#4A6B82; margin:10px 0;>Code : <span style="background:#E6F3FA; Color:#0077BE; padding:2px 8px; border-radius:5px;"> {code} | Section : {section}</p>

        """
    
    if stats:
        html+= """
        <div style="display:flex; gap:8px; flex-wrap:wrap;">
        """
        for icon, label, value in stats:
            html+= f'<div style="background: #0077BE15; padding: 5px 12px; border-radius: 12px; font-size:0.9rem">{icon} <b>{value}</b> {label} </div>'
        
    html += """
            </div>
        </div>
    """


    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()