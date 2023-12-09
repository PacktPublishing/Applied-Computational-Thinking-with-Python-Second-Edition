pastaAlfredo = 15.75
menu = {
    pastaAlfredo
    }
def priceIncrease(percentage):
    for item in menu:
        item = item + item * (percentage/100)
        print(round(item,2))
priceIncrease(30)
