import streamlit as st


def style_base_background():

    st.markdown("""
        <style>
               
               .stApp {
                    background: #F0F8FF !important;
                }
                
                .stTextInput div[data-baseweb="input],
                .stTextInput div[data-baseweb="base-input],
                .stTextInput > div > div {
                    background-color: #E6F3FA !important}
                .stApp div[data-testid="stColumn"] {
                    background-color: #FFFFFF !important;
                    padding: 1.5rem !important;
                    border-radius: 3rem !important;
                }
        </style>
                """
            ,unsafe_allow_html=True)


def style_base_dashboard():

    st.markdown("""
        <style>
               
               .stApp {
                    background: #F0F8FF !important;
                }  
        </style>   
            """
            ,unsafe_allow_html=True)

    
def style_base_layout():
#asdasd

    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Merriweather:ital,opsz,wght@0,18..144,300..900;1,18..144,300..900&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@200..800&family=Merriweather:ital,opsz,wght@0,18..144,300..900;1,18..144,300..900&display=swap');


         /* Hide Top Bar of streamlit */

            #MainMenu, footer, header {
                visibility: hidden;
            }

            [data-testid="stHeader"] {
                display: none !important;
            }

            [data-testid="stAppViewContainer"] {
                padding-top: 0 !important;
            }

            [data-testid="stAppViewBlockContainer"] {
                padding-top: 0 !important;
            }

            .block-container {
                padding-top: 0rem !important;
            } 
    
            h1 {
                font-family: "Manrope", sans-serif !important;
                font-size: 3.5rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
                color: #0077BE !important;
            }

            
            h2 {
                font-family: "Manrope", sans-serif !important;
                font-size: 2rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
                color: #0077BE !important;
            }

            h3, h4, p, label, li {
                font-family: 'Outfit', sans-serif !important;
                color: #003B5C !important;
            }

            
            button {
                border-radius: 1.5rem !important;
                background-color: #0077BE !important;
                color: #FFFFFF !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button[kind="secondary"] {
                border-radius: 1.5rem !important;
                background-color: #0077BE !important;
                color: #FFFFFF !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: all 0.25s ease-in-out !important;
            }

            button[kind="tertiary"] {
                border-radius: 1.5rem !important;
                background-color: #0077BE !important;
                color: #FFFFFF !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: all 0.25s ease-in-out !important;
            }
             
            button p {
                color: #FFFFFF !important;
            }

            button:hover{
                transform: scale(1.05) !important;
                background-color: #005F99 !important;
                color: #FFFFFF !important;
            }

            button[kind="secondary"]:hover{
                background-color: #005F99 !important;
                color: #FFFFFF !important;
            }

            button[kind="tertiary"]:hover{
                background-color: #005F99 !important;
                color: #FFFFFF !important;
            }

        </style>

                """
            ,unsafe_allow_html=True)