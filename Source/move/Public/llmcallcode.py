from openai import OpenAI
from pydantic import BaseModel

base_url = "https://api.aimlapi.com/v1"
api_key = "736e81f3713d49fb894ca482f4e7ae1b"
system_prompt = "Translate necessary parameters for the functions and return in given format., functions to move is moveTo with x,y,z coords"

api = OpenAI(api_key=api_key, base_url=base_url)

class jsonFormat(BaseModel):
    Location: list[float]

def get_ai_response(user_input: str) -> str:
    """Tar in en användarinput och returnerar svaret från OpenAI."""
    completion = api.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        response_format=jsonFormat,
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    user_input = input("Enter Prompt: ")
    response = get_ai_response(user_input)
    print("AI:", response)
