from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import os
from src.helper import load_pdf_files, filter_to_minimal_docs, text_split, downloadHF_embeddings

load_dotenv()


# load and process PDF Documents
print("Loading PDF files...")

extracted_data = load_pdf_files(
    data="data/"
)

print(f"Total pages loaded: {len(extracted_data)}")


# filter metadata
print("Filtering metadata...")

filtered_docs = filter_to_minimal_docs(
    extracted_data
)


# split the documents into smaller chunks
print("Splitting documents into chunks...")

text_chunks = text_split(
    filtered_docs
)

print(f"Total chunks created: {len(text_chunks)}")


# load embedding model

print("Loading embedding model...")

embeddings = downloadHF_embeddings()

print("Embedding model loaded successfully")


# create FAISS vector database from documents
print("Creating FAISS vector store...")

docsearch = FAISS.from_documents(
    documents=text_chunks,
    embedding=embeddings
)

print("FAISS vector store created successfully")



# save FAISS Index Locally
FAISS_INDEX_PATH = "faiss_index"

docsearch.save_local(
    FAISS_INDEX_PATH
)

print(f"FAISS index saved at: {FAISS_INDEX_PATH}")


print("Vector Database Creation Completed")