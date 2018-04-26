SCORE = float(input("Enter score: "))

if SCORE < 0:
    print("Invalid score")
elif SCORE > 100:
    print("Invalid score")
elif SCORE > 90:
    print("Excellent")
elif SCORE > 85:
    print("Destination")
elif SCORE > 50:
    print("Passable")
else:
    SCORE < 50
    print("Bad")
