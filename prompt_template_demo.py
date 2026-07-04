from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an interviewer.

Interview Technology:
{technology}

Experience:
{experience}

Ask only interview questions.
"""
        ),
        (
            "human",
            "{question}"
        )
    ]
)

prompt = template.invoke(
    {
        "technology": "Python",
        "experience": "5 Years",
        "question": "Start Interview"
    }
)

for message in prompt.messages:
    print(type(message))
    print(message.content)
    print("----------------")