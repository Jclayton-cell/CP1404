"""
CP1404
Broken program to determine score status
"""


def main():
    score = get_grade()
    print(score)

def get_grade():
    score = float(input("Enter score: "))
    if score > 100:
        grade = ("Invalid score")
    elif 0 <= score < 50:
        grade = ("Bad")
    elif 50 <= score < 90:
        grade = ("Passable")
    elif score >= 90:
        grade = ("Excellent")
    else:
        grade = ("Invalid score")
    return grade


main()
