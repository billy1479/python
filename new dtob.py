squarelist = [128,64,32,16,8,4,2,1]
hexvalue = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
values = [0,0]
def dtob(value):
    denary = int(value)
    length = len(squarelist)
    count = 0
    if denary > 255:
        print("Out of Range")
    for i in range(0,length):
        value = squarelist[i]
        answer = denary - value
        if answer >= 0:
            squarelist[count] = "1"
            denary = answer
        else:
            squarelist[count] = "0"
        count = count + 1
    s = ""
    binary = s.join(squarelist)
    return binary
def btod(value):
    total = 0
    binarylist = list(value)
    print(binarylist)
    length = len(binarylist)
    for i in range(0,length):
        temp = binarylist[i]
        if temp=="1":
            add = squarelist[i]
            total = total + add
        else:
            pass
    return total
def dtoh(value):
    denary = int(value)
    valueA = denary // 16
    valueB = denary % 16
    letterA = hexvalue[valueA]
    letterB = hexvalue[valueB]
    hexa = str(letterA) + str(letterB)
    return hexa
def htod(value):
    hexa = value
    letterA = hexa[0]
    letterB = hexa[1]
    for i in range(0,16):
        tempvalue = hexvalue[i]
        if tempvalue==letterA:
            valueA = i
        if tempvalue==letterB:
            valueB = i
    total = valueA * 16
    value = total + valueB
    return total
mode = str(input("What do you want to convert from? denary, hexa or binary : "))
if mode=="denary":
    value = input()
    values[0] = print(dtob(value))
    value = values[1]
    print(dtoh(value))
elif mode=="binary":
    value = input()
    values[0] = print(btod(value))
    value = values[0]
    print(dtoh(value))
elif mode=="hexa":
    value = input()
    print(htod(value))
    print(dtob(value))
    










    
