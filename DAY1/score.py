def score():
    while True:
        score = int(input("Enter Score between 0 to 100 : "))

        if score < 0 or score > 100 :
            print("Score is not valid")
            continue
        break

    if score <= 100 and score >= 90 :
        print("Grade obtained : A")
    elif score <= 89 and score >= 80 :
            print("Grade obtained : B")
    elif score <= 79 and score >= 70 :
            print("Grade obtained : C")
    elif score <= 69 and score >= 60 :
            print("Grade obtained : D")
    else:
          print("Grade Obtained : F")

score()
