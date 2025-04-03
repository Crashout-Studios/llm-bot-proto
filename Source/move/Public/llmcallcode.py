from openai import OpenAI
from pydantic import BaseModel
from typing import List, Dict, Union

api_key = ""
system_prompt = '''Translate necessary parameters for the functions and return in given format.,  
the move to location function is called move with parameters x,y,z, DET SKA ALLTID FINNAS tre parameterar (standardvärdet är X=1150 Y=490 Z=90)"
to make the character jump, jump har inga parametrar.

om spelaren ber om att få göra saker i rad. ex: gå till ett visst ställe, sen hoppa och sen gå till nästa ställe, varje del ska finnas i actions listan
'''

api = OpenAI(api_key=api_key)

class Action(BaseModel):
    name: str
    parameters: List[Union[str, float, int, List[float]]]  # Lista med olika typer av parametrar

class JsonFormat(BaseModel):
    actions: List[Action]

def get_ai_response(user_input: str) -> str:
    """Tar in en användarinput och returnerar svaret från OpenAI."""
    completion = api.beta.chat.completions.parse(
        model="gpt-4o-mini-2024-07-18",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        response_format=JsonFormat,
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    user_input = input("Enter Prompt: ")
    response = get_ai_response(user_input)
    print("AI:", response)
