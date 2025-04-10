import PIL.Image
import streamlit as st
import PIL as pil


with st.expander("Open Camera"):
    c_img = st.camera_input("Please use your camera")

if c_img:
    img = PIL.Image.open(c_img)
    gray_img = img.convert('L')
    st.image(gray_img)