def in_range(x: int, min: int, max: int) -> bool:
    return min <= x <= max


def assign_letter_grade(grade: int) -> str:
    if grade > 96:
        return "A+"
    elif in_range(grade, 93, 96):
        return "A"
    elif in_range(grade, 90, 92):
        return "A-"
    elif in_range(grade, 87, 89):
        return "B+"
    elif in_range(grade, 83, 86):
        return "B"
    elif in_range(grade, 80, 82):
        return "B-"
    elif in_range(grade, 77, 79):
        return "C+"
    elif in_range(grade, 73, 76):
        return "C"
    elif in_range(grade, 70, 72):
        return "C-"
    elif in_range(grade, 67, 69):
        return "D+"
    elif in_range(grade, 63, 66):
        return "D"
    elif in_range(grade, 60, 62):
        return "D-"
    else:
        return "F"
