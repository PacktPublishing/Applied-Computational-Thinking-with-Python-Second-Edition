state_capitals = {
    "Ohio" : "Columbus",
    "Alabama" : "Montgomery",
    "Arkansas" : "Little Rock"
    }
state_capitals["Iowa"] = "Des Moines"

state = input("What state's capital are you looking for today? ")
capital = state_capitals[state]


print("The capital of " + state + " is " + capital + ".")



