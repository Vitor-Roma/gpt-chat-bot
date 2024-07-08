from openai import OpenAI
from config import settings


def openai_chat_message(message):
    client = OpenAI(
        organization=settings.CHATGPT_ORGANIZATION_ID,
        project=settings.CHATGPT_PROJECT_ID,
        api_key=settings.CHATGPT_API_KEY
    )
    training = {"role": "system", "content": settings.CHATGPT_TRAINING_SCRIPT}

    messages = [training, {"role": "user", "content": message}]

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages
    )
    response = completion.choices[0].message.content
    print(response)
    return response


openai_chat_message("Hello! my name is Vitor, my password is 12345, i live in the 7th street, my ID is 54321 and my numbers are: 55 9338475-293232 and 9.0.8.9.7.4-.3.2.1.2.3.2. Also my car number is 123")
