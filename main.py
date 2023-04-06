import streamlit as st
import requests as rq
from bs4 import BeautifulSoup as bs

def main():
    st.markdown("<h1 style='text-align:center;color:LightSeaGreen;'>ImageMart<sub><a href='https://unsplash.com/' style='color:LightGreen;'>-Scrapped from UnSplash.com</a></sub></h1>",unsafe_allow_html=True)

    with st.form("search"):
        key = st.text_input(label="search images")
        if st.form_submit_button(label="Search"):
            page=rq.get(f"https://unsplash.com/s/photos/{key}")
            images=bs(page.content,"lxml").find_all("img",class_="tB6UZ a5VGX")
            src=lambda i : i["srcset"].split("?")[0]
            for i in images:
                st.image(src(i))
                
                
            
 # exicution starts from here            
if __name__=="__main__":
    main()
    