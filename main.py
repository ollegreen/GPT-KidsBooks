import os
import requests
import streamlit as st

from resources.api.api_key import the_api_key

st.write('Hello unknown storyteller!')

API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": f"{the_api_key}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

prompt = st.text_input('What story would you like?')


if prompt:
    output = query({
          "inputs": f"{prompt}",
          })
    st.write(output)
