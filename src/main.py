import random
import sys

import grading
import fileparser as parser
import history as hist_q_gen

history = parser.parse("questions/history.mc")
language = parser.parse("questions/language.mc")
math = parser.parse("questions/math.mc")
science = parser.parse("questions/science.mc")

letter_map = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25,
}

print("Welcome to a school test, something you probably haven't done in a while.")
print(
    "You will be asked how many questions of each subject you would like. You can put 0."
)


def get_question_count(subject):
    subject_question_count = 0
    question_count = input("How many {} questions would you like? ".format(subject))
    if question_count == "0":
        return 0
    else:
        try:
            subject_question_count = int(question_count)
        except ValueError:
            print("Please enter a number.")
            return get_question_count(subject)
        else:
            return subject_question_count


history_questions = get_question_count("history")
language_questions = get_question_count("language")
math_questions = get_question_count("math")
science_questions = get_question_count("science")

questions = []
total_questions = (
    history_questions + language_questions + math_questions + science_questions
)

correct_answers = 0
chosen_answers = []

if total_questions == 0:
    print("You have chosen to skip the test.")
    sys.exit(0)

if history_questions != 0:
    for x in range(history_questions):
        cap_q_chance = random.randint(1, 10)
        if cap_q_chance == 1:
            country = random.choice(list(hist_q_gen.country_capital_list.keys()))
            questions.append(hist_q_gen.capital_question(country))
        else:
            question = random.choice(history)
            questions.append(question)

if language_questions != 0:
    for x in range(language_questions):
        question = random.choice(language)
        questions.append(question)

if math_questions != 0:
    for x in range(math_questions):
        question = random.choice(math)
        questions.append(question)

if science_questions != 0:
    for x in range(science_questions):
        question = random.choice(science)
        questions.append(question)

for question in questions:
    print("\n" + question.question)
    for i, answer in enumerate(question.answers):
        print(list(letter_map.keys())[i] + ":", answer)
    letter = input("Enter the letter of your chosen answer: ")
    if question.correct_answer == question.answers[letter_map[letter]]:
        correct_answers += 1
    print()

score = round((correct_answers / total_questions) * 100)
print("You got an {}! ({})".format(grading.assign_letter_grade(score), score))
