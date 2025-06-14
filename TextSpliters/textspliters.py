from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(R"C:\Users\ACHISMAN\Desktop\Langchain models\2.Chat model\Books\AI_Topics.pdf")

docs = loader.load()


splitter = CharacterTextSplitter(chunk_size= 200 , chunk_overlap = 20 , separator = '')

result = splitter.split_documents(docs)

print(result[5].page_content)
