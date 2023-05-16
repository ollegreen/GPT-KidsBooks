import requests
import streamlit as st

st.write('Hello unknown storyteller!')

api_key = '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'

API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": f"{api_key}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

prompt = st.text_input('What story would you like?')


if prompt:
    output = query({
          "inputs": f"{prompt}",
          })
    st.write(output)
