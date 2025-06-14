from langchain_community.document_loaders import CSVLoader

Loader = CSVLoader(
    file_path = r"C:\Users\ACHISMAN\Desktop\Langchain models\2.Chat model\RAG\penguins.csv",
)

docs = Loader.load()

print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)