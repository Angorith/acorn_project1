import streamlit as st
from PIL import Image

def desc():
    st.markdown('#### Drawio 를 활용해 Dataflow 표시')
    image = Image.open('../project/images/dataflow.png')
    st.image(image, caption='-dataflow-')