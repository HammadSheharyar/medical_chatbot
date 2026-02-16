from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


# exctract data from pdf files in the "data" directory
def load_pdf_files(directory):
    loader = DirectoryLoader(
        directory, 
        glob="*.pdf", 
        #if u have multiple files, it will load all the pdf files in the directory
        loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents




from typing import List
from langchain_core.documents import Document

def filter_to_minimal(docs: List[Document]) -> List[Document]:
    minimal_docs: List[Document] = []
    for doc in docs:
        minimal_doc = Document(
            page_content=doc.page_content,
            metadata={"source": doc.metadata.get("source", "")}
        )
        minimal_docs.append(minimal_doc)
    return minimal_docs


def text_split(minimal_docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    text_chunks =  text_splitter.split_documents(minimal_docs)
    return  text_chunks
    
# embeddings and vector store
from langchain_huggingface import HuggingFaceEmbeddings

def create_embeddings():
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    return embeddings

