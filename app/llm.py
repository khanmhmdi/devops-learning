import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GAPGPT_API_KEY"),
    base_url="https://api.gapgpt.app/v1"
)

def call_llm(prompt: str) -> str:
    # response = client.chat.completions.create(
    #     model="gpt-4o",  # or gemini-2.5-pro, etc.
    #     messages=[
    #         {"role": "user", "content": prompt}
    #     ]
    # )


    # return response.choices[0].message.content
    return "HI, i am in test mode, i am not generated text from the LLM!"