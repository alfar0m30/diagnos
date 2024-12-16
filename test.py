def mathgame():

    points = 0
    answer = 7

    print("x * 6 = 42")
    guess = input("What is X? : ")

    if not guess.isdigit():
        print("that is not a digit, try again")
        return
    
    guess = int(guess)

    if guess == answer:
        points += 1
        print(f"That is correct! You now have {points} points!")

    else:
        print(f"Wrong, {guess} * 6 = {guess * 6}")
        if guess < answer:
            print("Your guess was too low...")
        else:
            print("Your guess was too high...")



mathgame();