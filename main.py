import random
min = 1 
max = 6 

roll_again = "Ja"

while roll_again == "Ja" or roll_again == "j": 
    print ("Dobbelen...")
    print ("De waarde is...")
    print (random.randint(min, max))
    roll_again = input("Wil je nog een keer dobbelen? (Ja of j)")