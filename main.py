import streamlit as st
from streamlit_option_menu import option_menu as opts
import base64
import webbrowser

from format_file import formatting
from home import display_home
from p_test import display_test

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
def set_background():
    img = get_img_as_base64("Background.png")
    page_bg_img = f"""
        <style>
        [data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/png;base64,{img}");
        background-size: 100%;
        background-repeat: no-repeat;
        background-attachment: local;
        }}
        </style>
        """     
    st.markdown(page_bg_img, unsafe_allow_html=True)

def main():
    formatting()
    set_background()
    st.title('PERSONALITY')
    st.header("Group 6 - DSEB 65B")
    with st.sidebar:
        selected = opts(
            menu_title = None,
            options = ['Home', 'Personality Test', 'Personality Types', 'Contact Us'],
            icons = ['house', 'person', 'star', 'envelope'],
            default_index=0,
            styles={"container": {"padding": "0!important", "background-color": "#0d0c0c"},
                    "icon": {"color": "white", "font-size": "25px"},
                    "nav-link": {
                        "font-size": "15px",
                        "text-align": "left",
                        "margin": "0px",
                        "--hover-color": "#ffe8e8",
                    },
                "nav-link-selected": {"background-color": "pink"},
            }
        )
    if selected == 'Home':
        display_home()
    if selected == 'Personality Test':
        display_test()
if __name__ == "__main__":
    main()