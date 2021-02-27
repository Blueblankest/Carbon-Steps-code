#Initialize Variables
steps = int(input("number of steps taken"))
plastic = False
cans = False
reuse = False
recycle = False
single_driver = False
bus = False
bike = False
carpool = False
points = 0
#Increment/Decrement Stuff
def increment():
    global points
    global plastic
    global cans
    global reuse
    global recycle
    global single_driver
    global bus
    global bike
    global carpool
    if steps % 1000 == 0:
        points -= (steps/1000)
    if plastic == True:
        points += 2
        plastic = False
    if cans == True:
        points += 1
        cans = False
    if reuse == True:
        points -= 1
        reuse = False
    if recycle == True:
        points -= 1
        recycle = False
    if single_driver == True:
        points += 5
        single_driver = False
    if bus == True:
        points += 1
        bus = False
    if bike == True:
        points += 1
        bike = False
    if carpool == True:
        points +=2
        carpool = False


#Tester
plastic = True
cans = True

increment()
print(steps)
print(points)

