from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage
)
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from config import CHAT_MODEL,GOOGLE_API_KEY

load_dotenv()

llm = ChatGoogleGenerativeAI(model=CHAT_MODEL, google_api_key=GOOGLE_API_KEY)

messages = [
    SystemMessage(
        content="You are a helpful assistant."
    ),

    HumanMessage(
        content="My name is Dharmendra."
    ),

    AIMessage(
        content="Nice to meet you, Dharmendra!"
    ),

    HumanMessage(
        content="What is my name?"
    )
]

response = llm.invoke(messages)

print(response.content)