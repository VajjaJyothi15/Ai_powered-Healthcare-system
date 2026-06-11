from config.settings import GROQ_API_KEY

try:
    from groq import Groq
except ModuleNotFoundError:
    Groq = None


client = Groq(api_key=GROQ_API_KEY) if Groq and GROQ_API_KEY else None


def get_ai_response(prompt):

    if client is None:
        return (
            "The advanced chatbot is unavailable in this environment. "
            "I can still help with appointments, symptoms, medicines, and reports."
        )

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
