# Web Content RAG Assistant

A Retrieval-Augmented Generation (RAG) application that allows users to analyze web content and ask questions about it using GPT-4 Turbo.

## Features

- Load and analyze web page content from URLs
- Store content in a persistent vector database
- Ask questions about the loaded content using GPT-4 Turbo
- User-friendly Streamlit interface

## Requirements

- Python 3.11
- OpenAI API key

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
```bash
cp .env.example .env
```
Edit `.env` and add your OpenAI API key.

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided URL (typically http://localhost:0709)

3. Enter a webpage URL and click "Load Webpage" to analyze its content

4. Ask questions about the loaded content using the question input field

## Project Structure

- `app.py`: Main Streamlit application
- `utils/`
  - `web_scraper.py`: Web content scraping functionality
  - `vector_store.py`: Vector database management
  - `rag_chain.py`: RAG chain implementation
- `requirements.txt`: Project dependencies
- `.env`: Environment variables (API keys)

## Notes

- The vector database is persisted in the `./chroma_db` directory
- Web content is stored across sessions
- The application uses GPT-4 Turbo for optimal performance
