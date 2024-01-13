import streamlit as st #this page is the main page called first page, the rest pages should come in another folder
from streamlit_extras.switch_page_button import switch_page #importing 

bg_img= """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1541855951501-fc42a85d86d3?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
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
st.set_page_config(initial_sidebar_state="collapsed") #values always come in inverted commas, this line allows sidebar to be collapsed, it always comes before title

st.markdown(bg_img, unsafe_allow_html=True)
st.title("HOME")
st.write("Welcome,")
st.write("My name is Neil Jhunjhunwala and I created this website. This website enables users to identify the content of the inputted image, which should depict something related to nature or Earth.")
st.write("To make it easier, this website allows users to identify images using object-orinted dectection based on 4 specific classifications.")
st.header("")
st.subheader("Please click on the button corresponding to the classification you would like to try.")
st.markdown("(You can also use the sidebar panel to navigate to the specified page)")
if st.button("Dog Breed Classification"):
    switch_page("Dog Breed Classification") #inside quotes should be name of second page
if st.button("Mammal Classification"):
    switch_page("Mammal Classification")
if st.button("Moth Classification"):
    switch_page("Moth Classification")
if st.button("Natural Features Classification"):
    switch_page("Natural Features Classification")

st.header("")
st.header("")
st.write("To know more about the creation of the models used for object detection, click the button below")
if st.button("Know more") :
    switch_page("About")
