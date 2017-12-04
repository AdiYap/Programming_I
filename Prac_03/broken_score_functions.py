"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def score_status(score):
    status = ""
    if score < 0:
        status = "Invalid score"
    else:
        if score > 100:
            status = "Invalid score"
        elif score >= 90:
            status = "Excellent"
        elif score >= 50:
            status = "Passable"
        elif score < 50:
            status = "Bad"
    return status

score = float(input("Enter score: "))
status = score_status(score)
print(status)

exit(0)