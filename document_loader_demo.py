from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import PDF_PATH

loader = PyPDFLoader(PDF_PATH)

documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

chunks = splitter.split_documents(documents)

print("Total Chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print("=" * 50)
    print("Chunk:", i + 1)
    print(chunk.page_content)