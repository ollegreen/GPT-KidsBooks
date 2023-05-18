import os
from langchain.llms import OpenAI
import streamlit as st
from langchain.documents_loaders import PyPDFLoader
from langchain.vectorstores import Chroma

from langchain.agents.agent_toolkits import (
    create_vectorstore_agent,
    VectorStoreToolkit,
    VectorStoreInfo
)

os.environ['OPENAI_API_KEY'] = the_secret_sauce_openai

# Create instance of OpenAI LLM
llm = OpenAI(temperature=0.8, verbose=True)

# Create and load PDF Loader
loader = PyPDFLoader('data/kids_story.pdf')

# Split pages from pdf
pages = loader.load_and_split()

# Load documents into vector database aka ChromaDB
store = Chroma.from_documents(pages, collection_name='kids_story')

# Create vectorstore info object - metadata repo?

vectorstore_info = VectorStoreInfo(
    name="kids_story",
    description="a bedtime story for kids as a pdf",
    vectorstore=store
)

# Convert the document store into a langchain toolkit
toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info)

# Add the toolkit to an end-to-end LC
agent_executor = create_vectorstore_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)

st.title('🦜🔗 GPT KidsBooks')
# Create a text input box for the user
prompt = st.text_input('Input your wanted storyline here')

# If the user hits enter
if prompt:
    # Then pass the prompt to the LLM
    response = agent_executor.run(prompt)
    # ...and write it out to the screen
    st.write(response)

    # With a streamlit expander
    with st.expander('Document Similarity Search'):
        # Find the relevant pages
        search = store.similarity_search_with_score(prompt)
        # Write out the first
        st.write(search[0][0].page_content)