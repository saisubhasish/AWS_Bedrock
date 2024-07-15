import requests
import streamlit as st

from src.logger import logging
from src.exception import BlogException

def get_bedrock_response(blog_topic):
    try:
        logging.info("'main': Post request to the backend API with given data")
        response = requests.post(
            "https://f5z0m20hu5.execute-api.us-east-1.amazonaws.com/dev/blog_generation",
            json={
                'blog_topic': blog_topic
            }
        )
        logging.info(f"'main': Request response: {response}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

st.title('Blog Generator')

with st.form("my_form"):
    st.write("Fill the input fields below: ")
    blog_topic = st.text_input('Enter the topic name')
    logging.info(f"'main': Topic name: {blog_topic}")

    submitted = st.form_submit_button("Submit")
    if submitted:
        logging.info("'main': Data submitted, now invoking the Backend API")
        response = get_bedrock_response(blog_topic)
        logging.info(f"'main': Generated response: {response}")
        if 'error' in response:
            st.error(f"Error: {response['error']}")
        else:
            st.write(response)

st.write("Thank you for using the blog generator.")