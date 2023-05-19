import openai
import json # Import the json module

API_KEY = "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"

openai.api_key = API_KEY

asks = 0
questions = input("How many questions do you want to ask? ")
while asks < int(questions):
    asks += 1
    query = input("\n Ask anything: ")
    response = openai.Completion.create(
    prompt=str(query),
    model="text-davinci-003",
    temperature=0.9,
    max_tokens=150,
    )
    data = json.loads(str(response)) # Parse the JSON object into a Python dictionary
    text = data["choices"][0]["text"] # Get the text value from the dictionary
    print(text) # Print the text value
    rem = int(questions) - asks
    print("\n You have " + str(rem) + " questions left")

print("\n\n -----Thank you for using this program!-----")