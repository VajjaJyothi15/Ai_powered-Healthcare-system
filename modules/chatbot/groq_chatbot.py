from groq import Groq

from config.settings import (
    GROQ_API_KEY
)

client = Groq(
    api_key=GROQ_API_KEY
)


def get_ai_response(prompt):

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content":
                """
                You are a healthcare AI assistant.
                Provide general healthcare guidance.
                Never diagnose patients.
                Always recommend consulting a doctor.
                """
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=500
    )

    return completion.choices[0].message.content