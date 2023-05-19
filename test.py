import openai
import json # Import the json module
import time

API_KEY = "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"

openai.api_key = API_KEY

ts = time.time()

myName = input("What is your name? ")

# print(open(fileName, "a"))

start = "-\n\n---Welcome " + myName + " to the AI Exam question generator!--- \n"
print(start)

##answer a few questions before starting
print("-->Answer a few questions before we start \n")

institution = input("What institution are you in? (U - university, H - high school, C - college, M - middle school, E - elementary school) \n >")

if institution.capitalize() == "U":
    ins = "university"
elif institution.capitalize() == "H":
    ins = "high school"
elif institution.capitalize() == "C":
    ins = "college"
elif institution.capitalize() == "M":
    ins = "middle school"
elif institution.capitalize() == "E":
    ins = "elementary school"


grade = input("What grade are you in? (1 - 4) \n >")
if grade == "1":
    grade = "1st"
elif grade == "2":
    grade = "2nd"
elif grade == "3":
    grade = "3rd"
elif grade == "4":
    grade = "4th"
else:
    grade = "1st"

subject = input("What subject are you in? (M - math, E - english, S - science, H - history, K - Kiswahili, P - Physics, C - Chemistry, B - Biology, A - Arts, O - Other) \n >")

if subject.capitalize() == "M":
    sub = "math"
elif subject.capitalize() == "E":
    sub = "english"
elif subject.capitalize() == "S":
    sub = "science"
elif subject.capitalize() == "H":
    sub = "history"
elif subject.capitalize() == "K":
    sub = "Kiswahili"
elif subject.capitalize() == "P":
    sub = "physics"
elif subject.capitalize() == "C":
    sub = "chemistry"
elif subject.capitalize() == "B":
    sub = "biology"
elif subject.capitalize() == "A":
    sub = "arts"
elif subject.capitalize() == "O":
    sub = "other"
else:
    sub = "math"

level = input("What level are you in? (B - basic, I - intermediate, A - advanced) \n >")
if level.capitalize() == "B":
    lv = " basic"
elif level.capitalize() == "I":
    lv = " intermediate"
elif level.capitalize() == "A":
    lv = " advanced"
else:
    lv = " basic"

asks = 0
questions = input("How many questions do to be tested on? (1-5) \n >")


fileName = "./tests/test_" + myName + "_" + ins + "_" + grade + "_" + sub + "_" + lv + "_" +  str(ts) + ".txt"
start = "----Welcome " + myName + " to the AI Exam question generator!---- \n\n"
with open(fileName, "a") as file:
    file.write(start)

info = "You are in a " + ins + " \n"
print(info)
with open(fileName, "a") as file:
    file.write(info)

info = "You are in the " + grade + " grade \n"
print(info)
with open(fileName, "a") as file:
    file.write(info)

info = "You have chosen the subject of " + sub + " \n"
print(info)
with open(fileName, "a") as file:
    file.write(info)

info = "You have chosen the " + lv + " level \n"
print(info)
with open(fileName, "a") as file:
    file.write(info)

info = "You have chosen to be tested on " + questions + " questions \n\n"
print(info)
with open(fileName, "a") as file:
    file.write(info)

info = "--------------------Start Your Test Below-------------------- \n"
print(info)
with open(fileName, "a") as file:
    file.write(info)

while asks < int(questions):
    asks += 1

    query = "Generate a " + lv + " level "+ grade + " grade " + sub + " question for a " + ins + " student "
    response = openai.Completion.create(
    prompt=str(query),
    model="text-davinci-003",
    temperature=0.9,
    max_tokens=150,
    )
    data = json.loads(str(response)) # Parse the JSON object into a Python dictionary
    text = data["choices"][0]["text"] # Get the text value from the dictionary
    text_question = "Question:" + str(asks) + text + " \n"
    with open(fileName, "a") as file:
        file.write(text_question)

    # input("Press Enter to continue.")

    query2 = "in 50 words or less answer " + text + " as a " + ins + " student"
    response2 = openai.Completion.create(
    prompt=str(query2),
    model="text-davinci-003",
    temperature=0.9,
    max_tokens=50,
    )
    data2 = json.loads(str(response2)) # Parse the JSON object into a Python dictionary
    text2 = data2["choices"][0]["text"] # Get the text value from the dictionary
    # print("answer prompt: " + str(asks) + query2)
    # print("Answer " + text2)
    tt3 = "Question answer:" + text2 + " \n"
    with open(fileName, "a") as file:
        file.write(tt3)

    print (text)
    my_answer = input("Answer>")
    tt4 = "\n Students answer:" + my_answer + " \n"
    with open(fileName, "a") as file:
        file.write(tt4)

    
    query3 = "in 50 words or less compare " + my_answer + " with " + text2 + " if the first answer is correct reply with 'your answer is correct' if the first answer is incorrect reply with 'your answer is incorrect' and explain why"
    response3 = openai.Completion.create(
    prompt=str(query3),
    model="text-davinci-003",
    temperature=0.9,
    max_tokens=150,
    )
    data3 = json.loads(str(response3)) # Parse the JSON object into a Python dictionary
    text3 = data3["choices"][0]["text"] # Get the text value from the dictionary
    tt4 = "About Your Question :" + text3 + " \n"
    with open(fileName, "a") as file:
        file.write(tt4)


    cut = "------------------------------------------------------ \n\n"
    with open(fileName, "a") as file:
        file.write(cut)

    rem = int(questions) - asks
    print("\n You have " + str(rem) + " questions left")

print("\n\n -----Thank you for using this program!-----")


tt4 = "-----Thank you for using this program!-----"
with open(fileName, "a") as file:
    file.write(tt4)

open(fileName, "a").close()