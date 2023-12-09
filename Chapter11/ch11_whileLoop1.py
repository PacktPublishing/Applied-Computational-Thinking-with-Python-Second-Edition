myAnimals = []
print('Let\'s see how many animals you can name. Get ready!')
readyPlayer = input('When you are ready to begin, type y. ')
while readyPlayer == 'y':
    animalAdd = input('Name an animal. ')
    myAnimals.append(animalAdd)
    readyPlayer = input('Ready for the next one? Type y for yes or n for no. ')
howMany = len(myAnimals)
print(f'You were able to name {howMany} animals. Here\'s your list: ')
print(myAnimals) 