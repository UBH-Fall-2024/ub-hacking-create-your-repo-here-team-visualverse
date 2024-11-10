import streamlit as st
import os
import requests
import time

# Create a directory to store the uploaded images
UPLOAD_DIR = "src/sample_img"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Function to make a POST request
def make_post_request(file):
    # Simulate a POST request with a delay to show the loader
    #time.sleep(3)  # Simulate the delay of the request
    # Assuming you want to send the file as part of the request
    url = "http://0.0.0.0:8000/get_caption"  # Replace with your actual API URL
    response = requests.post(url, json={'name': file})
    return response.json()  # Assuming the response is in JSON format

# Streamlit app

st.markdown("""
    <style>
   body{
       background: rgba(181, 120, 216, 0.1);
   }
    
    
    </style>
""", unsafe_allow_html=True)

st.title("VisualVerse.ai")

# Image upload widget
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Save the uploaded image to the directory
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Show a loader while making the POST request
    with st.spinner("Sending the image and waiting for response..."):
        response_data = make_post_request(uploaded_file.name)
    
    # Show the response data after the request completes
    if response_data["des"] == "err":
         st.write("Error in Image use another image")
    st.success("Request Completed!")
    st.write(f"Image Caption : {response_data['cap']}")
    st.write(f"Image Description : {response_data['des']}")
    
    # Optionally display the uploaded image
    st.image(file_path, caption="Uploaded Image", use_column_width=True)
