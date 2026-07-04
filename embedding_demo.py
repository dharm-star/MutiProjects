import os

from dotenv import load_dotenv

from langchain_google_genai import GoogleGenerativeAIEmbeddings

from config import EMBEDDING_MODEL

load_dotenv()

embedding_model = GoogleGenerativeAIEmbeddings(
    model=EMBEDDING_MODEL
)

text = "Kafka is a distributed streaming platform."

embedding = embedding_model.embed_query(text)

print(type(embedding))
print(len(embedding))

print(embedding[:10])