import random


class MultipleChoiceQuestion:
    """A class to represent a multiple choice question."""

    def __init__(self, question: str, answers: list) -> None:
        self.question = question
        if len(answers) == 0:
            raise ValueError("Answers list cannot be empty.")
        self.correct_answer = answers[0]
        random.shuffle(answers)
        self.answers = answers


def parse(file_name):
    """Parses a specific question file (extension must be .mc or .fb) and returns the questions."""
    ext = file_name.split(".")[-1]
    questions = []
    if ext == "mc":
        question = ""
        answers = []
        with open(file_name, "r") as f:
            lines = [line.removesuffix("\n") for line in f.readlines()]
        for i, line in enumerate(lines):
            if line.startswith("Q::"):
                question = line[3:].strip()
            elif line.startswith("A::"):
                answers = line[3:].strip().split(",,")

            if answers != []:
                questions.append(MultipleChoiceQuestion(question, answers))

    elif ext == "fb":
        pass
    else:
        raise ValueError("Invalid file extension: " + ext)
