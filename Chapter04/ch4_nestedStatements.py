number = int(input("Pick a number between 1 and 20. "))
if number < 10:
    if number < 6:
        print("Why such a small number?")
    else:
        print("Well, less than 10 but greater than 5. I'll take it.")
elif number < 21:
    if number < 16:
        print("You like values that are greater than 10, but not too much greater. I guess that's fine.")
    else:
        print("I like larger numbers myself too.")
else:
#Sometimes we make mistakes when providing input in programs. If you choose a number that's not between 0 and 20, the program will print this message.
    print("That number isn't between 0 and 20. Run the program and try again.")
