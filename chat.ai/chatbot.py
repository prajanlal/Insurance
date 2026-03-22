# pip install google-genai

import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key="AIzaSyA1c-AW1ptrgM1gPTnCvjV9fX7n2OgdZ_s"   
    )

    config = types.GenerateContentConfig(
        temperature=0.5,
        max_output_tokens=200,   
        safety_settings=[
            types.SafetySetting(
                category="HARM_CATEGORY_HARASSMENT",
                threshold="BLOCK_ONLY_HIGH",
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_HATE_SPEECH",
                threshold="BLOCK_ONLY_HIGH",
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
                threshold="BLOCK_ONLY_HIGH",
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_DANGEROUS_CONTENT",
                threshold="BLOCK_ONLY_HIGH",
            ),
        ],
        system_instruction=types.Part.from_text(text="""
You are a professional AI insurance assistant.

- Help users understand insurance (health, life, vehicle, travel)
- Explain policies, premiums, claims clearly
- Recommend plans based on user needs
- Speak simply and politely
- Keep answers under 80 words
- Use short sentences
- Do not give long introductions
""")
    )

    chat = client.chats.create(
        model="gemini-flash-latest",
        config=config
    )

    print(" Insurance Assistant Ready! Type 'exit' to stop.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Chat ended.")
            break

        response = chat.send_message(user_input)

        print("Bot:", response.text)
        print()


if __name__ == "__main__":
    generate()
