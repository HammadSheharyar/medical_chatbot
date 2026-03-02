# medical_chatbot
 pip install python-multipart
for fastapi

...existing code...

# medical_chatbot

Lightweight medical question-answering chatbot using PDF sources, embeddings, Pinecone vector store, Groq LLM, and a FastAPI + Bootstrap frontend.

## Quick Start

create Conda environment:
```sh
conda create -n chabot python=3.11 -y
conda activate chabot
```


1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    
    ```

2. Configure environment variables (export or put in `.env`):
    ```sh
    export PINECONE_API_KEY="your-pinecone-key"
    export GROQ_API_KEY="your-groq-key"
    ```
  

3. Build the Pinecone index (process PDFs in [data]):
    ```sh
    python store_index.py
    ```

4. Run the web app:
    ```sh
    uvicorn app:app --reload
    ```
   Open http://127.0.0.1:8000/

## What this app uses

- FastAPI backend: [app.py](http://_vscodecontentref_/3). Endpoints:
  - [app.index](http://_vscodecontentref_/4) — serves the chat page.
  - [`app.chat[](app.py) — POST ](http://_vscodecontentref_/5)/get` chat endpoint invoked by the frontend.
- Indexing and vector store: [store_index.py](http://_vscodecontentref_/6)
- PDF loading, splitting, and embeddings: functions in [src/helper.py](http://_vscodecontentref_/7):
  - [src.helper.load_pdf_files](http://_vscodecontentref_/8)
  - [src.helper.filter_to_minimal](http://_vscodecontentref_/9)
  - [src.helper.text_split](http://_vscodecontentref_/10)
  - [src.helper.create_embeddings](http://_vscodecontentref_/11)
- Prompt template: [src.prompt.system_prompt](http://_vscodecontentref_/12)
- Frontend template: [templates/chat.html](http://_vscodecontentref_/13)
- Styling: [static/style.css](http://_vscodecontentref_/14)
- Packaging metadata: [setup.py](http://_vscodecontentref_/15)

## How it works (overview)

1. PDF ingestion
   - PDFs from the [data](http://_vscodecontentref_/16) directory are loaded with [src.helper.load_pdf_files](http://_vscodecontentref_/17).
2. Minimalization & chunking
   - Documents are normalized by [`src.helper.filter_to_minimal[](src/helper.py) and split into chunks via [](http://_vscodecontentref_/18)src.helper.text_split`](src/helper.py).
3. Embeddings & Index
   - Embeddings created by [`src.helper.create_embeddings[](src/helper.py) (HuggingFace model ](http://_vscodecontentref_/19)sentence-transformers/all-MiniLM-L6-v2`).
   - [store_index.py](http://_vscodecontentref_/20) creates/updates a Pinecone index and uploads embeddings. See [store_index.py](http://_vscodecontentref_/21).
4. Retrieval & RAG
   - App loads vector store with [PineconeVectorStore](http://_vscodecontentref_/22) and creates a retriever + RAG chain in [app.py](http://_vscodecontentref_/23).
   - System prompt is defined in [src.prompt.system_prompt](http://_vscodecontentref_/24).
5. UI
   - The chat interface in [templates/chat.html](http://_vscodecontentref_/25) sends user messages via AJAX to [/get](http://_vscodecontentref_/26) and renders responses. Styles located in [static/style.css](http://_vscodecontentref_/27).

## Folder structure



