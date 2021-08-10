import random
from pprint import pprint


class MultipleChoiceQuestion:
    """A class to represent a multiple choice question."""

    def __init__(self, question: str, answers: list) -> None:
        self.question = question
        if len(answers) == 0:
            raise ValueError("Answers list cannot be empty.")
        self.correct_answer = answers[0]
        self.answers = answers
        random.shuffle(self.answers)


def parse(file_name):
    """Parses a specific question file (extension must be .mc or .fb) and returns the questions."""
    ext = file_name.split(".")[-1]
    if ext == "mc":
        questions = []
        with open(file_name, "r") as f:
            lines = [line.removesuffix("\n") for line in f.readlines()]
            for line in lines:
                answers = []
                if line.startswith("Q: "):
                    question = line[3:].strip()
                elif line.startswith("A: "):
                    answers = line[3:].strip().split(",,")

                if answers != []:
                    mcq = MultipleChoiceQuestion(question, answers)
                    questions.append(mcq)
    else:
        raise ValueError("Invalid file extension: " + ext)
    return questions
