import os
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

prompt = PromptTemplate(
    template = "Answer the following questions based on the given text:\n\nQuestions:\n{questions}\n\nText:\n{text}",
    input_variables = ['questions','text']
)

# Set a user agent string
os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

url = "https://www.amazon.ca/Samsung-A16-6-7-Android-Unlocked-Warranty/dp/B0DP5LSL9Q"
loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt| model|parser

result = chain.invoke({'questions' : 'what is the name of the products?', 'text' : docs[0].page_content})

print(result)