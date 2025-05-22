import json


with open('files/quiz.json', 'r') as file:
    quiz = json.load(file)


user_correct = 0


for q in quiz['quiz']:
    print(q['question'])
    for index, option in enumerate(q['alternatives']):
        print(f"{index + 1}. {option}")
    get_answer = input("Enter the number of correct answer: ")
    get_answer = int(get_answer) - 1
    if get_answer < 0 or get_answer >= len(q['alternatives']):
        print("Invalid answer. Please enter a number corresponding to the options.")
        continue
    user_answer = q['alternatives'][get_answer]
    if user_answer == q['correct_answer']:
        print("Correct!")
        user_correct += 1
    else:
        print("Incorrect!")    
    
if user_correct > 0:
    average =user_correct / len(quiz['quiz'])
    print(f"Your average score is: {average:.2f}")
else:
    print("You didn't answer any questions correctly.")