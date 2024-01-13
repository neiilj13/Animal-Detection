import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import streamlit as st
from PIL import Image
from ultralytics import YOLO
bg_img= """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1509023464722-18d996393ca8?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
background-size: cover;
}

[data-testid="stHeader"] {
background-color: rgba(0,0,0,0);
}
[data-testid="stToolbar"] {
right: 2rem;
}

[data-testid="stSidebar"]{
background-image: url("https://images.unsplash.com/photo-1634118931958-f1cf1f9c6156?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
background-size: cover;
}
/<style>
"""
st.title('Dog Breed Classification')
st.markdown(bg_img, unsafe_allow_html=True)
@st.cache_resource #helps in preventing excessing memory, only loads model once
def load_model_2():
	mod=YOLO(r"C:\Users\neilj\Desktop\IB DAIS NEILJ\COLLEGE\MACHINE LEARNING\home\dogbreed_classify_medium_20_288_32.pt")
	return mod

img = st.file_uploader('Select the image', type=['jpg','png','jpeg'])
if img is not None:
	img = Image.open(img)
	st.markdown('Image Visualization')
	st.image(img) 
	st.markdown("<h1 style='text-align: center; color: white;'>Results</h1>", unsafe_allow_html=True)
	model=load_model_2()
	res=model.predict(img)
	label=res[0].probs.top5
	conf=res[0].probs.top5conf
	conf=conf.tolist()

	col1,col2 = st.columns(2)
	col1.subheader(res[0].names[label[0]] +' with '+ str(conf[0])+' Confidence')
	col1.subheader(res[0].names[label[1]] +' with '+ str(conf[1])+' Confidence')
	col1.subheader(res[0].names[label[2]] +' with '+ str(conf[2])+' Confidence')
	col2.subheader(res[0].names[label[3]] +' with '+ str(conf[3])+' Confidence')
	col2.subheader(res[0].names[label[4]] +' with '+ str(conf[4])+' Confidence')
	

