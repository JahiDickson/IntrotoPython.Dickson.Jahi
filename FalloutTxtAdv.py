import random

print("Welcome to Fallout Wasteland!")
print("You are lost in the Wasteland caused by the nuclear fallout with your car.")
print("You recently found some people who turned out to be a group of psychopath cannibals who want to eat you and your car!")
print("Survive the Wasteland and outrun the psychopaths.")
print()

# Variables
milesTraveled = 0
thirst = 0
nuclearpower = 100
cannibalsTraveled = -30
canteen = 3
grocerystore = 0
fatigue = 0
nuclearfuelcellbreakcahnce = 0
cartotaledchance = 0
killedincarcrash = 0
nocar = 0
chancetofindcar = 0
carbreakdownchance = 0
done = False

# Start main loop
while not done and nocar == 0:
    cannibalsBehind = milesTraveled - cannibalsTraveled
    fullSpeed = random.randrange(15, 30)
    moderateSpeed = random.randrange(10, 20)

    print("A. Drink from your canteen.")
    print("B. Ahead at moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check")
    print("Q. Quit.")
    print()

    userInput = raw_input("Your choice? ")

    if userInput.lower() == "q":
        done = True

    # Status
    elif userInput.lower() == "e":
        print("Miles traveled:", milesTraveled)
        print("Drinks in canteen:", canteen)
        print("Fatigue level:", fatigue)
        print("Your car has", nuclearpower, "power.")
        print("The cannibals are", cannibalsBehind, "miles behind you.")
        print("Your thirst is", thirst)

    # Stop for night
    elif userInput.lower() == "d":
        fatigue *= 0
        thirst += 1
        print("You feel refreshed and happy that your fatigue is now", fatigue)
        cannibalsTraveled += random.randrange(15, 22)

    # Move full speed
    elif userInput.lower() == "c":
        print("You traveled", fullSpeed, "miles")
        milesTraveled += fullSpeed
        thirst += 1
        nuclearpower -= 40
        cannibalsTraveled += random.randrange(13, 21)
        grocerystore = random.randrange(1, 21)
        fatigue += 1
        carbreakdownchance = random.randrange(1,21)

    # Move moderate speed
    elif userInput.lower() == "b":
        print("You traveled", moderateSpeed, "miles")
        milesTraveled += moderateSpeed
        thirst += 1
        nuclearpower -= 20
        cannibalsTraveled += random.randrange(13, 21)
        grocerystore = random.randrange(1, 21)
        fatigue += 1
        carbreakdownchance = random.randrange(1, 41)

    # Drink canteen
    elif userInput.lower() == "a":
        if canteen == 0:
            print("You're out of water.")
        else:
            canteen -= 1
            thirst *= 0
            print("You have", canteen, "drinks left and you are no longer thirsty.")

    # Not done check
    if grocerystore == 20:
        thirst *= 0
        canteen = 3
        print("You found an anbandoned grocery store!") 
        print("After taking a drink and eating you looted it of it's supplies and filled your canteen and replaced your fuel cell.")
        
    if carbreakdownchance == 30:
        nocar += 1
        print("Your car broke down while driving it.")
        print("You have to travel by foot!")

    if cannibalsBehind <= 15:
        print("The cannibals are drawing near!")

    if milesTraveled >= 1000 and not done:
        print("You made it across the wasteland, you win!")
        done = True

    if cannibalsTraveled >= milesTraveled:
        print("The cannibals caught and ate you.")
        print("You're dead!")
        done = True

    if thirst > 4 and thirst <= 6 and not done:
        print("You are thirsty")

    if thirst > 6:
        print("You died of dehydration!")
        done = True

    if nuclearpower > 1 and nuclearpower <= 20 and not done:
        print("You're running out of gas.")

    if nuclearpower < 0:
        print("You're out of gas!")
        print("You have to travel by foot.")
        nocar += 1
        
    if fatigue < 8 and fatigue > 5:
        print("You are getting tired.")
        
    if fatigue > 8:
        print("You fell asleep while driving and crashed into something off road.")
        cartotaledchance = random.randrange(1, 3)
        killedincarcrash = random.randrange(1, 10)
    
        if cartotaledchance == 2:
            print ("You totaled your car and have to go by foot!")
            nocar += 1
        
        if killedincarcrash == 9:
            print("You died in the crash!")
            done = True

while not done and nocar > 0:
    cannibalsBehind = milesTraveled - cannibalsTraveled
    fullSpeed = random.randrange(2, 4)
    moderateSpeed = random.randrange(1, 2)
    
    print("A. Drink from your canteen.")
    print("B. Ahead at moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check")
    print("Q. Quit.")
    print()
    
    if userInput.lower() == "q":
        done = True

    # Status w/nocar
    elif userInput.lower() == "e":
        print("Miles traveled:", milesTraveled)
        print("Drinks in canteen:", canteen)
        print("Fatigue level:", fatigue)
        print("The cannibals are", cannibalsBehind, "miles behind you.")
        print("Your thirst is", thirst)
        print("You have no car!")

    # Stop for night w/nocar
    elif userInput.lower() == "d":
        fatigue *= 0
        thirst += 2
        chancetofindcar = random.randrange(1, 30)
        print("You feel refreshed and happy that your fatigue is now", fatigue)
        cannibalsTraveled += random.randrange(15, 22)

    # Move full speed w/nocar
    elif userInput.lower() == "c":
        print("You traveled", fullSpeed, "miles")
        milesTraveled += fullSpeed
        thirst += 3
        fatigue += 3
        cannibalsTraveled += random.randrange(15, 22)
        grocerystore = random.randrange(1, 41)
        chancetofindcar = random.randrange(1, 11)

    # Move moderate speed w/nocar
    elif userInput.lower() == "b":
        print("You traveled", moderateSpeed, "miles")
        milesTraveled += moderateSpeed
        thirst += 2
        fatigue += 2
        cannibalsTraveled += random.randrange(15, 22)
        grocerystore = random.randrange(1, 61)
        chancetofindcar = random.randrange(1, 16)

    # Drink canteen w/nocar
    elif userInput.lower() == "a":
        if canteen == 0:
            print("You're out of water.")
        else:
            canteen -= 1
            thirst *= 0
            print("You have", canteen, "drinks left and you are no longer thirsty.")

    # Not done check w/nocar
    if grocerystore == 20:
        thirst *= 0
        canteen = 3
        nuclearpower = 200
        print("You found an anbandoned grocery store!") 
        print("After taking a drink and eating you looted it of it's supplies and filled your canteen.")
        
    if chancetofindcar == 10:
        nocar = 0
        badcar = random.randrange(1,10)
        print ("You found a working car! You put your gas into the car and get back to driveing")

    if cannibalsBehind <= 15:
        print("The cannibals are drawing near!")

    if milesTraveled >= 1000 and not done:
        print("You made it to civilization and safety, you win!")
        done = True

    if fatigue < 8 and fatigue > 5:
        print("You are getting tired.")

    if cannibalsTraveled >= milesTraveled:
        print("The cannibals caught and ate you.")
        print("You're dead!")
        done = True

    if thirst > 4 and thirst <= 6 and not done:
        print("You are thirsty")

    if thirst > 6:
        print("You died of dehydration!")
        done = True
