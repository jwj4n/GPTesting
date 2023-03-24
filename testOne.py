import openai
from key import OPENAI_KEY
openai.api_key = OPENAI_KEY

question = input("Ask me anything: ")

response = openai.Completion.create(
    model="ada",
    prompt = question,
)

# Raw feedback, not conversational
print(response)
