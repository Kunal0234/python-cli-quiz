questions =[ {
    "question": "What is Python?",
    "options": ["Programming Language", "Database", "Operating System", "Web Browser"],
    "answer": 1
},{
   "question": "Who developed Python  Programming Language?",
       "options": ["Wick van Rossum", "Rasmus Lerdorf", "Guido van Rossum", "Niene Stom"],
       "answer": 3 
},{
   "question": "Which type of Programming does Python support?",
       "options": ["object-oriented  programming", "structured programming", "functional programming", "all of the mentioned"],
       "answer": 4 
},{
   "question": "Which of the following is used to define a block of code in Python language?",
       "options": ["Indentation", "Key", "Brackets", "All of the mentioned"],
       "answer": 1 
},{
   "question": "Which keyword is used for function in Python language?",
       "options": ["Function", "def", "Fun", "Define"],
       "answer": 2 
},{
   "question": "Which of the following character is used to give single-line comments in Python?",
       "options": ["//", "#", "!", "/*"],
       "answer": 2 
},{
   "question": "What does pip stand for python?",
       "options": ["Pip Installs Python", "Pip Installs Packages", "Preferred Installer Program", "All of the mentioned"],
       "answer": 3 
},{
   "question": "Which of the following functions is a built-in function in python?",
       "options": ["factorial()", "print()", "seed()", "sqrt()"],
       "answer": 2
},{
   "question": "Which of the following is not a core data type in Python programming?",
       "options": ["Tuples", "Lists", "Class", "Dictionary"],
       "answer": 3
},{
   "question": "What arithmetic operators cannot be used with strings in Python?",
       "options": ["*", "-", "+", "All of the mentioned"],
       "answer": 2 
}]
print("==============================\n    PYTHON CLI QUIZ  \n============================== \n")
print("Welcome to the python Quiz!\n")
print("You will answer multiple-choice questions.")
print("Let's begin!\n")

def run_quiz():
 current_score = 0
 for index,question in enumerate(questions):
    print(f"{index+1}.{question["question"]}\n")
    for option_index, option in enumerate(question["options"]):
     print(option_index+1,option)
    answer = int(input("\nEnter your answer:- "))
    if answer == question['answer']:
      print("Correct!✅")
      current_score +=1
      print(f"Current Score : {current_score}\n")
      
    else:
      print("Wrong answer!❌")
      print(f"Current Score :{current_score}\n")

 print(f"Your Total score is :- {current_score}")
run_quiz()