from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template = "Summaraize the following text in 3 bullet points - {text}",
    input_variables=["text"]
)

parser = StrOutputParser()




loader = TextLoader("C:/Users/ACHISMAN/Desktop/Langchain models/2.Chat model/RAG/Ai.txt", encoding="utf-8")


documents = loader.load()

print(type(documents[0]))

print(len(documents))

print(documents[0].page_content)

print(documents[0].metadata)

chain = prompt | model | parser

result= chain.invoke({"text" : documents[0]})

print(result)

