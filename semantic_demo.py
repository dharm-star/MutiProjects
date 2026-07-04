from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai import GoogleGenerativeAIEmbeddings



# ------------------------
# Load PDF
# ------------------------
documents = PyPDFLoader("data/notes.pdf").load()

# ------------------------
# Character Splitter
# ------------------------
char_splitter = RecursiveCharacterTextSplitter(
    chunk_size=120,
    chunk_overlap=20,
)

char_chunks = char_splitter.split_documents(documents)

print("=" * 80)
print("CHARACTER CHUNKS")
print("=" * 80)

for i, chunk in enumerate(char_chunks, start=1):
    print(f"\nChunk {i}")
    print("-" * 40)
    print(chunk.page_content)

# ------------------------
# Semantic Splitter
# ------------------------
embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001",api_key="AIzaSyDhI4fGIHqhA87nJnu3srou5yPg6v0l7jI")  # Replace

semantic_splitter = SemanticChunker(
    embeddings=embedding_model
)

semantic_chunks = semantic_splitter.split_documents(documents)

print("\n")
print("=" * 80)
print("SEMANTIC CHUNKS")
print("=" * 80)

for i, chunk in enumerate(semantic_chunks, start=1):
    print(f"\nChunk {i}")
    print("-" * 40)
    print(chunk.page_content)