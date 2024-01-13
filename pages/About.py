import streamlit as st
from streamlit_extras.switch_page_button import switch_page
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
st.title("ABOUT")
st.markdown(bg_img, unsafe_allow_html=True)
st.write("The inspiration to create this website started from able to create an object detection model trained to detect anything around you. Unfortunately, to make something like this, you need immense amounts of computing power as well as accurate data sets which I did not have access to.")
st.write("Intially, I tried scavaging whatever data sets and I landed on 4 good ones. The earlier version of this website, was combining the 4 various models trained into one and instead of the user picking which classification, the model does it on its own (I will be adding this section soon to the website).")
st.header("")
st.write("I used YOLO classification to train and test my 4 models. It took lot of tweaking of the batch size, epoch number, as well as image size to get the best model. Information about the code as well as data on training the model for each data set is given below.")
st.write("")
st.subheader("1. Dog Breed Classfication")
st.write("Number of Epochs: 20")
st.write("Image size: 288")
st.write("Batch size: 32")
st.subheader("2. Mammal Classfication")
st.write("Number of Epochs: 20")
st.write("Image size: 288")
st.write("Batch size: 32")
st.subheader("3. Moth Classfication")
st.write("Number of Epochs: 20")
st.write("Image size: 320")
st.write("Batch size: 34")
st.subheader("4. Natural Features Classfication")
st.write("Number of Epochs: 20")
st.write("Image size: 288")
st.write("Batch size: 32")
st.header("")
st.markdown("Lastly, the training times varied from 8-20 hours depending on the classification. Factors playing a role into training times were number of images in datasets as well as computing power of the device I was using. I have mentioned the technical details of the computing device used below.")
st.subheader("Technical Details of device used to train models")
st.write("CPU: Ryzen 9 5900HS (16 core)")
st.write("GPU: RTX 3060 + AMD Radeon (8 GB VRAM in Total)")
st.write("RAM: 16GB")
st.header("")
st.subheader("More additions to the website will be coming soon...")
