import os
import streamlit as st


st.title('🦜🔗 GPT KidsBooks')
# Create a text input box for the user
prompt = st.text_input('Input your wanted storyline here')


# Print the output
print('\n',tokenizer.decode(output[0]))

# If the user hits enter
if prompt:
    
    st.write(f"you want this model to do the following: {response}")
