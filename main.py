#Initialize Variables
steps = int(input("number of steps taken"))
plastic = False
cans = False
reuse = False
points = 0
#Increment/Decrement Stuff
def increment():
    global points
    global plastic
    global cans
    global reuse
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

#Tester
plastic = True
cans = True
increment()
print(steps)
print(points)

