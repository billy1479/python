#park cars
a = 0
b = 0
values = [0,0]

def randomplacement():
    import random
    x = random.randint(1,rown - 1)
    y = random.randint(1,columnn - 1)
    park[x][y] = 'ABCDEFG'
    
def empty(a,b):
    allowed = False
    if park[a][b] == "Empty":
        allowed = True
        park[a][b] = registration
        message = True
    else:
        allowed = False
        print("This space is taken, please ask again.")
        message  = False
    return message

def rangecheck(r,c):
    counter = 0
    rangev = False
    r = r - 1
    c = c - 1
    while rangev==False:
        if r < 0 and c < 0 and r > rown and c > columnn:
            rangev = False
            print("Please enter the right range")
            r = int(input("Enter the row you want to check : "))
            c = int(input("Enter the column you want to check : "))
        else:
            rangev = True
            values[0] = r
            values[1] = c
            return values

def findcar(registration):
    position = False
    for i in range(0,rown):
        for x in range(0, columnn):
            if park[i][x] == registration:
                position = True
                print("The car has been found")
                print("The car is at posision " + str(i+1) + "," + str(x+1))
    if position!=True:
        print("Car was never found")

def display(park):
    print('')
    print('')
    print('')
    spacelist = []
    for i in range(0,rown):
        templist = []
        temp = park[i]

        for x in range(columnn):
            space = "     "
            length = len(temp[x])
            if length > 5:
                index = length - 5
                for y in range(0,index + 1):
                    spacelist.append(" ")
                space = "".join(spacelist)
                templist.append(temp[x])
                templist.append(space)
            elif length < 5:
                index = 10 - length
                for y in range(0, index):
                    spacelist.append(" ")
                space = ''.join(spacelist)
                templist.append(temp[x])
                templist.append(space)
            else:    
                templist.append(temp[x])
                templist.append(space)
        if (i+1) >= 10:
            print(str(i + 1) + ": " + ("".join(templist)))
        else:
            print(str(i + 1) + ":  " + ("".join(templist)))
    
def lengthcheck(registration):
    t = 0
    while t == 0:
        if len(registration) > 7:
            print("Length of registation out of range")
            registration = str(input("Enter registration : "))
        else:
            return registration

        
rown = int(input("Enter number of rows : "))
columnn = int(input("Enter number of columns : "))
t = 0

park = [0] * rown
for i in range(0,rown):
    park[i] = ["Empty"] * columnn

while t == 0:
    mode = str(input("Do you want to find or enter a car? "))
    if mode=="enter":
        r = int(input("Enter the row you want to check : "))
        c = int(input("Enter the column you want to check : "))
        rangecheck(r,c)
        a = values[0]
        b = values[1]
        registration = str(input("Enter registration : "))
        registration = lengthcheck(registration)
        empty(a,b)
        t = 1
        display(park)
    elif mode=="find":
        randomplacement()
        registration = str(input("Enter registration number :"))
        lengthcheck(registration)
        findcar(registration)
        t = 1
        display(park)
    else:
        print("Enter the right mode. ")
        t = 0

