import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import streamlit_app as st
from dotenv import load_dotenv
import os

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

from langchain_core.prompts import ChatPromptTemplate

from src.prompt import system_prompt

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


# streamlit page config
st.set_page_config(
    page_title="Medical ChatBot",
    page_icon="🩺",
    layout="centered"
)


# page title
st.title("🩺 Medical ChatBot")
st.markdown(
    "Ask any medical-related question from the PDF knowledge base."
)


# load embedding model
@st.cache_resource
def load_embeddings():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embeddings


# load faiss vector database
@st.cache_resource
def load_vectorstore():

    embeddings = load_embeddings()

    vectorstore = FAISS.load_local(
        "faiss_index",
        embeddings=embeddings,
        allow_dangerous_deserialization=True
    )

    return vectorstore


# load llm
@st.cache_resource
def load_llm():

    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="llama-3.3-70b-versatile",
        temperature=0
    )

    return llm


# create RAG chain
@st.cache_resource
def create_chain():
    vectorstore = load_vectorstore()

    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )

    llm = load_llm()

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}")
        ]
    )

    question_answer_chain = (
        create_stuff_documents_chain(
            llm,
            prompt
        )
    )

    rag_chain = create_retrieval_chain(
        retriever,
        question_answer_chain
    )

    return rag_chain


# user input
user_question = st.text_input(
    "Enter your medical question:"
)

# generate response
if user_question:

    with st.spinner("Generating response..."):
        rag_chain = create_chain()
        response = rag_chain.invoke(
            {
                "input": user_question
            }
        )

        st.subheader("Answer")

        st.write(response["answer"])