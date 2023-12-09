firstNumber = int(input('Enter a number between 0 and 3: '))

if(firstNumber < 4):
        secondNumber = int(input('Enter a number between 8 and 15: '))
        if(secondNumber > 7 and secondNumber < 16):
            sum1 = firstNumber + secondNumber
            print("I predict your number is less than 19, in this case", sum1)
        else:
            print("Run this again and pay attention to the numbers!")
else:
    print("Run this again and pay attention to the numbers!")



