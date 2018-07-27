import random

print("Welcome to Fallout Wasteland!")
print("You are lost in the Wasteland caused by the nuclear fallout with your car.")
print("You recently found some people who turned out to be a group of psychopath cannibals who want to eat you and your car!")
print("Survive the Wasteland and outrun the psychopaths.")
print()

# Variables
milesTraveled = 0
fullSpeed = 0
moderateSpeed = 0
fullspeedonfoot = 0
thirst = 0
nuclearpower = 200
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
findpowerincarset = 0
findpowerincarchance = 0
powerpumped = 0
done = False

# Start main loop
while not done and nocar <= 0 :
    cannibalsBehind = milesTraveled - cannibalsTraveled
    fullSpeed = random.randrange(15, 35)
    moderateSpeed = random.randrange(10, 25)

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
        print("Your thirst is", thirst)
        print("Your car has", nuclearpower, "power.")
        print("The cannibals are", cannibalsBehind, "miles behind you.")

    # Stop for night
    elif userInput.lower() == "d":
        fatigue *= 0
        thirst += 1
        print("You feel refreshed and happy that your fatigue is now", fatigue)
        cannibalsTraveled += random.randrange(15, 21)

    # Move full speed
    elif userInput.lower() == "c":
        print("You traveled", fullSpeed, "miles")
        milesTraveled += fullSpeed
        thirst += 1
        nuclearpower -= 60
        cannibalsTraveled += random.randrange(13, 21)
        grocerystore = random.randrange(1, 31)
        fatigue += 1
        carbreakdownchance = random.randrange(1,21)
        findpowerincarset += fullSpeed
        findpowerincarchance = random.randrange(1, 5)
        
    # Move moderate speed
    elif userInput.lower() == "b":
        print("You traveled", moderateSpeed, "miles")
        milesTraveled += 25
        thirst += 1
        nuclearpower -= 30
        cannibalsTraveled += random.randrange(13, 21)
        grocerystore = random.randrange(1, 36)
        fatigue += 1
        carbreakdownchance = random.randrange(1, 31)
        findpowerincarset += moderateSpeed
        findpowerincarchance = random.randrange(1, 9)

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
        powerpumped = random.randrange(50, 150)
        if nocar == 0:
            nuclearpower += powerpumped
        print("You found an anbandoned grocery store!") 
        print("After taking a drink and eating you looted it of it's supplies and filled your canteen and put power into your fuel cell")
    
    if findpowerincarchance == 4:
        print ("You found an unused car!")
        print ("You you took the power from the nuclear fuel cell and put into your car!")
        powerpumped = random.randrange(25, 100)
        nuclearpower += powerpumped
        
    if findpowerincarset >= 100:
        print ("You found an unused car!")
        print ("You you took the power from the nuclear fuel cell and put into your car!")
        powerpumped = random.randrange(25, 100)
        nuclearpower += powerpumped
        findpowerincarset = 0
        
    if carbreakdownchance == 8:
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

    if thirst > 5 and thirst <= 8 and not done:
        print("You are thirsty")

    if thirst > 8:
        print("You died of dehydration!")
        done = True

    if nuclearpower > 1 and nuclearpower <= 20 and not done:
        print("You're running out of gas.")

    if nuclearpower <= 0:
        print("Your car is out of power!")
        print("You have to travel by foot.")
        nocar += 1
        if nuclearpower < 0:
            nuclearpower = 0
        
    if fatigue < 8 and fatigue > 5:
        print("You are getting tired.")
        
    if fatigue > 8:
        print("You fell asleep while driving and crashed into something off road.")
        cartotaledchance = random.randrange(1, 3)
        killedincarcrash = random.randrange(1, 10)
    
        if cartotaledchance == 2 and killedincarcrash != 9:
            print ("You totaled your car and have to go by foot!")
            nocar += 1
        
        if killedincarcrash == 9 and cartotaledchance != 2:
            print("You died in the crash!")
            done = True
            
        if killedincarcrash == 9 and cartotaledchance == 2:
            print("You died in the crash!")
            done = True

# Loop w/ no car
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
    
    userInput = raw_input("Your choice? ")
    
    if userInput.lower() == "q":
        done = True

    # Status w/ no car
    elif userInput.lower() == "e":
        print("Miles traveled:", milesTraveled)
        print("Drinks in canteen:", canteen)
        print("Fatigue level:", fatigue)
        print("The cannibals are", cannibalsBehind, "miles behind you.")
        print("Your thirst is", thirst)
        print("You have", nuclearpower, "power.")
        print("You have no car!")

    # Stop for night w/ no car
    elif userInput.lower() == "d":
        fatigue *= 0
        thirst += 1
        print("You feel refreshed and happy that your fatigue is now", fatigue)
        cannibalsTraveled += random.randrange(15, 22)

    # Move full speed w/ nocar
    elif userInput.lower() == "c":
        print("You traveled", fullSpeed, "miles")
        milesTraveled += fullSpeed
        thirst += 4
        fatigue += 4
        cannibalsTraveled += random.randrange(15, 22)
        grocerystore = random.randrange(1, 41)
        chancetofindcar = random.randrange(1, 6)
        findpowerincarset += fullspeedonfoot

    # Move moderate speed w/ no car
    elif userInput.lower() == "b":
        print("You traveled", moderateSpeed, "miles")
        milesTraveled += moderateSpeed
        thirst += 3
        fatigue += 3
        cannibalsTraveled += random.randrange(15, 22)
        grocerystore = random.randrange(1, 61)
        chancetofindcar = random.randrange(1, 11)
        findpowerincarset += moderateSpeed

    # Drink canteen w/ no car
    elif userInput.lower() == "a":
        if canteen == 0:
            print("You're out of water.")
        else:
            canteen -= 1
            thirst *= 0
            print("You have", canteen, "drinks left and you are no longer thirsty.")

    # Not done check w/ no car
    if grocerystore == 20:
        thirst *= 0
        canteen = 3
        nuclearpower = 200
        print("You found an anbandoned grocery store!") 
        print("After taking a drink and eating you looted it of it's supplies and filled your canteen.")
    
    if findpowerincarset >= 100:
        print ("You found an unused car!")
        print ("You you took the power from the nuclear fuel cell and put into your car!")
        powerpumped = random.randrange(25, 100)
        nuclearpower += powerpumped
        findpowerincarset = 0
        
    if chancetofindcar == 5:
        print ("You found a working car! You get in and get back to driving")
        nocar -= 1
        nuclearpower += random.randrange(20, 30)
       
    if cannibalsBehind <= 30:
        print("The cannibals are drawing near!")

    if milesTraveled >= 1000 and not done:
        print("You made it to civilization and safety, you win!")
        done = True

    if fatigue < 8 and fatigue > 5:
        print("You are getting tired.")
        
    if fatigue > 8:
        print("You passed out from lack of rest!")
        print("The cannibals catch and eat you!")

    if cannibalsTraveled >= milesTraveled:
        print("The cannibals caught and ate you.")
        print("You're dead!")
        done = True

    if thirst > 5 and thirst <= 8 and not done:
        print("You are thirsty")

    if thirst > 8:
        print("You died of dehydration!")
        done = True
