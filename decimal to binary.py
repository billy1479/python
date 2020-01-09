print("Please enter one of the modes : 1 is decimal to binary, 2 is binary to hexadecimal, 3 is hexadecimal to denary, 4 is denary to hexadecimal, 5 is hexadecimal to binary")
mode = int(input("Enter the the mode number : "))


squarelist = [128,64,32,16,8,4,2,1]
squarelist2 = [8,4,2,1]
hexvalue = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
length = len(squarelist)
if mode==1:
    #decimal to binary
    print("This converts decimal to binary")
    newnumber = int(input("Enter the decimal number : "))
    count = 0
    if newnumber > 255:
        print("Wrong value entered")
    for i in range(0, length):
        value = squarelist[i]
        answer = newnumber - value
        if answer >= 0:
            squarelist[count] = 1
            newnumber = answer
        else:
            squarelist[count] = 0
        count = count + 1
    print(squarelist)
elif mode==2:
    #binary to hexadecimal
    print("This is the hexadecimal conversion from the binary : ")
    total1 = 0
    total2 = 0
    counter = 0
    usersquarelist1 = [8,4,2,1]
    usersquarelist2 = [8,4,2,1]
    binarylist = str(input("Enter binary here : "))
    binarylist = list(binarylist)
    for i in range(0,8):
        binaryvalue = binarylist[i]
        if i < 4:
            print("value being assigned to usersquarelist1 is " + binaryvalue)
            usersquarelist1[counter] = binaryvalue
        elif i > 3:
            print("value being assigned to usersquarelist2 is " + binaryvalue)
            usersquarelist2[counter] = binaryvalue
        counter = counter + 1
        if counter > 3:
            counter = 0
    for x in range(0,4):
        tempvalue = int(usersquarelist1[x])
        print(str(tempvalue))
        index = squarelist2[x]
        if tempvalue==1:
            print("adding " + str(index))
            total1 = total1 + index
    x = 0
    for x in range(0,4):
        tempvalue = int(usersquarelist2[x])
        print(str(tempvalue))
        index = squarelist2[x]
        if tempvalue==1:
            print("adding " + str(index))
            total2 = total2 + index
    letterA = hexvalue[total1]
    letterB = hexvalue[total2]
    print("Letter A is " + str(letterA))
    print("Letter B is " + str(letterB))
elif mode==3:
    userhex = str(input("Enter the Hex value : "))
    listhex = list(userhex)
    letterA = listhex[0]
    letterB = listhex[1]
    #hexadecimal to denary
    Avalue = 0
    Bvalue = 0
    for i in range(0,16):
        temphex = hexvalue[i]
        if letterA==temphex:
            Avalue = int(i)
            print("match")
        if letterB==temphex:
            Bvalue = int(i)
            print("match")
    total = 16 * Avalue
    total = total + Bvalue
    print("The decimal value of " + str(userhex) + " is " + str(total))
elif mode==4:
    print("This converts a denary number to its hexadecimal equivalent...")
    number = int(input("Enter the denary number : "))
    tempvalue = number // 16
    letterA = hexvalue[tempvalue]
    tempvalue = number % 16
    letterB = hexvalue[tempvalue]
    print("Letter A is " + str(letterA))
    print("Letter B is " + str(letterB))
elif mode==5:
    list1 = [0,0,0,0]
    list2 = [0,0,0,0]
    finallist = [0,0,0,0,0,0,0,0]
    count = 0
    print("This converts hexadecimal values into binary...")
    hexnumber = str(input("Enter the hexadecimal value here : "))
    hexlist = list(hexnumber)
    letterA = hexlist[0]
    letterB = hexlist[1]
    for i in range(0,16):
        tempvalue = hexvalue[i]
        if tempvalue==letterA:
            valueA = int(i)
        if tempvalue==letterB:
            valueB = int(i)
    for x in range(0,4):
        if count > 3:
            count = 0
        tempvalue = squarelist2[x] 
        newvalue = valueA - tempvalue
        if newvalue >= 0:
            list1[count] = 1
            valueA = newvalue
        else:
            list1[count] = 0
        count = count + 1
    for x in range(0,4):
        if count > 3:
            count = 0
        tempvalue = squarelist2[x] 
        newvalue = valueB - tempvalue
        if newvalue >= 0:
            list2[count] = 1
            valueB = newvalue
        else:
            list2[count] = 0
        count = count + 1
    for y in range(0,4):
        index1 = list1[count]
        index2 = list2[count + 4]
        finallist[y] = index1
        finallist[y + 4] = index2
        if count==4:
            count = 0
        
            
        
    
        
            
        

    
    

    

    

    

    
    
        
