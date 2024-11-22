"""Main Streamlit application for the RAG web content analyzer."""
import streamlit as st
import os
from dotenv import load_dotenv
from utils.web_scraper import scrape_webpage
from utils.vector_store import VectorStoreManager
from utils.rag_chain import RAGChain

# Load environment variables
load_dotenv()

# Set page configuration
st.set_page_config(
    page_title="Web Content RAG Assistant",
    page_icon="🌐",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .stButton > button {
        background-color: #ff4b4b;
        color: white;
    }
    .main {
        background-color: #f0f2f6;
    }
    .st-emotion-cache-1v0mbdj {
        background-color: #e6e9f0;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if 'vector_store' not in st.session_state:
    st.session_state.vector_store = VectorStoreManager(persist_directory="./chroma_db")
if 'rag_chain' not in st.session_state:
    st.session_state.rag_chain = RAGChain(st.session_state.vector_store.vector_store)
if 'webpage_content' not in st.session_state:
    st.session_state.webpage_content = None

# Title and description
st.title("🌐 Web Content RAG Assistant")
st.markdown("""
    Enter a webpage URL to analyze its content and ask questions about it.
    The assistant uses GPT-4 Turbo to provide accurate answers based on the webpage content.
""")

# URL input
url = st.text_input("Enter webpage URL:", placeholder="https://example.com")

# Load webpage button
if st.button("Load Webpage"):
    if url:
        with st.spinner("Loading webpage content..."):
            content = scrape_webpage(url)
            if content:
                st.session_state.webpage_content = content
                st.success("Webpage content loaded successfully!")
                
                # Store content in vector store
                st.session_state.vector_store.add_texts([content], [{"source": url}])
                st.success("Content stored in vector database!")
            else:
                st.error("Failed to load webpage content. Please check the URL and try again.")
    else:
        st.warning("Please enter a URL first.")

# Display webpage content if available
if st.session_state.webpage_content:
    with st.expander("View Webpage Content"):
        st.text_area("Content", st.session_state.webpage_content, height=200)

# Question answering section
st.markdown("---")
st.header("Ask Questions")
question = st.text_input("Enter your question about the webpage content:", placeholder="What is the main topic discussed?")

if st.button("Get Answer"):
    if question:
        if st.session_state.webpage_content:
            with st.spinner("Generating answer..."):
                answer = st.session_state.rag_chain.query(question)
                st.markdown("### Answer")
                st.write(answer)
        else:
            st.warning("Please load a webpage first before asking questions.")
    else:
        st.warning("Please enter a question.")
