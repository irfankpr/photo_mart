import streamlit as st
import requests as rq
from bs4 import BeautifulSoup as bs

def main():
    st.markdown("<h1 style='text-align:center;color:LightSeaGreen;'>ImageMart<sub><a href='https://unsplash.com/' style='color:grey;'>-Scrapped from UnSplash.com</a></sub></h1>",unsafe_allow_html=True)
    col1,col2,col3=st.columns([1,2,1])
    with col2.form("search"):
        key = st.text_input(label="search images")
        submit=st.form_submit_button(label="Search",use_container_width=True)
    canvas=st.empty()
    c1,c2,c3,c4=canvas.columns(4)
    if submit:
        page=rq.get(f"https://unsplash.com/s/photos/{key}")
        images=bs(page.content,"lxml").find_all("img",class_="tB6UZ a5VGX")[:10]
        src=lambda i : i["srcset"].split("?")[0]
        for n,img in enumerate(images):
            if n%4==0:
                c1.image(src(img))
            elif n%4==1:
                c2.image(src(img))
            elif n%4==2:
                c3.image(src(img))
            else :
                c4.image(src(img))
                    
                
            
                
                
            
 # exicution starts from here            
if __name__=="__main__":
    st.set_page_config(layout="wide")
    main()
    