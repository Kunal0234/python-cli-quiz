import random
import json
print("==============================\n    PYTHON CLI QUIZ  \n============================== \n")
print("Welcome to the python Quiz!\n")
print("You will answer multiple-choice questions.")
print("Let's begin!\n")
name = input("Enter your name :-  ")
print(f"Welcome {name}! Lets's start the quiz")

with open("questions.json", "r") as file:
    questions = json.load(file)
def run_quiz():
    current_score = 0
    random.shuffle(questions)

    for index, question in enumerate(questions):
        print(f"{index + 1}. {question['question']}\n")

        for option_index, option in enumerate(question["options"]):
            print(option_index + 1, option)

        while True:
            try:
                answer = int(input("\nEnter your answer:- "))
                if  1<=answer<=4:
                    break
                else:
                    print("Please enter a valid option (1-4)!")
                    continue
                
            except ValueError:
                print("Please enter a number!")

        if answer == question['answer']:
            print("Correct!✅")
            current_score += 1
            print(f"Current Score : {current_score}\n")

        else:
            print("Wrong answer!❌")
            print(f"Current Score : {current_score}\n")
    print("========== QUIZ RESULT ==========\n")
    print(f"{name}, Your Total score is :- {current_score}/10")
    print(f"Percentage : {(current_score/10)*100}%")
    if current_score >= 4:
        print("Result : Passed\n")
    else:
        print("Result : Failed\n") 
    print("=================================")

while True:
    
    run_quiz()

    while True:
        run_again = input("Do you want to play again? (y/n): ").lower()

        if run_again == "y":
            break
        elif run_again == "n":
            exit()
        else:
            print("Please enter y or n\n")

