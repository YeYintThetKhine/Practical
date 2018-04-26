def main():
    score = float(input("Enter score: "))
    score_check(score)
    print(score_check(score))


def score_check(score):
    if 0 > score or score > 100:
        return "Invalid Score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
