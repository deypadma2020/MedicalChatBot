from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq

from dotenv import load_dotenv
import os

from src.helper import downloadHF_embeddings
from src.prompt import system_prompt


load_dotenv()


def create_rag_chain():

    # load embeddings
    embeddings = downloadHF_embeddings()


    # load vector database
    vectorstore = FAISS.load_local(
        "faiss_index",
        embeddings=embeddings,
        allow_dangerous_deserialization=True
    )


    # create retriever
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )


    # load llm
    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile",
        temperature=0
    )


    # create prompt
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}")
        ]
    )


    # create question answer chain
    question_answer_chain = create_stuff_documents_chain(
        llm,
        prompt
    )


    # create rag chain
    rag_chain = create_retrieval_chain(
        retriever,
        question_answer_chain
    )

    return rag_chain