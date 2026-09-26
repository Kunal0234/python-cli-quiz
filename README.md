# 🐍 Python CLI Quiz

A command-line multiple-choice quiz application built with Python.
The quiz loads questions from a JSON file, randomizes the question order, validates user input, tracks the score, and displays the final result.

## ✨ Features

* 🎯 Multiple-choice Python questions
* 🔀 Random question order
* 👤 Player name input
* ✅ Correct/wrong answer feedback
* 🔢 Input validation
* 🚫 Validates options between 1-4
* 📊 Live score tracking
* 📈 Final score percentage
* 🏆 Pass/Fail result
* 🔁 Replay the quiz
* 📄 Questions stored in a JSON file
* 🧩 Quiz logic organized using Python functions

## 🛠️ Technologies Used

* Python
* JSON
* Random module

## 📁 Project Structure

```text
python-cli-quiz/
│
├── main.py
├── questions.json
└── README.md
```

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/Kunal0234/python-cli-quiz.git
```

2. Open the project folder:

```bash
cd python-cli-quiz
```

3. Run the quiz:

```bash
python main.py
```

## 🎮 How It Works

1. Enter your name.
2. Questions are loaded from `questions.json`.
3. Questions appear in random order.
4. Select an answer between `1-4`.
5. The program validates your input.
6. Your score is updated after every question.
7. At the end, your score, percentage, and result are displayed.
8. You can choose to play again.

## 📌 Example

```text
========== QUIZ RESULT ==========

Kunal, Your Total score is :- 7/10
Percentage : 70.0%
Result : Passed

=================================
```

## 🚧 Project Status

**Completed — Version 1.0**

Future improvements may include:

* Quiz categories
* Difficulty levels
* High-score tracking
* More questions
* Further code refactoring

## 👨‍💻 Author

**Kunal Singh**

Built as a Python learning project to practice:

* Python fundamentals
* Functions
* Lists and dictionaries
* Loops and conditions
* Exception handling
* JSON file handling
* Randomization
* Git and GitHub
