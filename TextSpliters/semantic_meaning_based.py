from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text_splitter = SemanticChunker(
    OpenAIEmbeddings(),
    breakpoint_threshold_type='standard_deviation',  # fixed param name
    breakpoint_threshold_amount=1
)

text = """Artificial Intelligence (AI) is revolutionizing the healthcare industry..."""

docs = text_splitter.create_documents([text])

print(docs[0].page_content)

print(docs[0].metadata)


