from langchain_community.document_loaders import PyPDFLoader

Loader = PyPDFLoader(r"C:\Users\ACHISMAN\Desktop\Langchain models\2.Chat model\RAG\AI_in_Healthcare_25Pages.pdf")

documents = Loader.load()

print(documents[0].page_content)

print(documents[0].metadata)
