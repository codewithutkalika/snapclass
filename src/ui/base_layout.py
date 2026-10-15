import streamlit as st


def style_base_background():

    st.markdown("""
        <style>
               
               .stApp {
                    background: #E6E6FA !important;
                }
                
                .stApp div[data-testid="stColumn"]{
                    background-color: #FFFFFF !important;
                    padding:1.5rem !important;
                    border-radius:3rem !important;
                }
        </style>

                """
            ,unsafe_allow_html=True)


def style_base_dashboard():

    st.markdown("""
        <style>
               
               .stApp {
                    background: #D6D0F5 !important;
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
            }

            
            h2 {
                font-family: "Manrope", sans-serif !important;
                font-size: 2rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
            }

            h3, h4, p, {
                font-family: 'Outfit', sans-serif !important;
            }

            
            button {
                border-radius: 1.5rem !important;
                background-color: #B47A98 !important;
                color: #FFFFFF !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button[kind="secondary"] {
                border-radius: 1.5rem !important;
                background-color: #A83D68 !important;
                color: #FFFFFF !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: all 0.25s ease-in-out !important;
            }

            button[kind="tertiary"] {
                border-radius: 1.5rem !important;
                background-color: #E6DDEB !important;
                color: #5C4B65 !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: all 0.25s ease-in-out !important;
            }
             
            button:hover{
                transform: scale(1.05) !important;
                background: #9F6687 !important;
            }

            button[kind:"secondary"]:hover{
                background: #B5A3CF !important;
            }

            button[kind:"tertiary"]:hover{
                background: #D5C7DD !important;
            }

        </style>

                """
            ,unsafe_allow_html=True)
