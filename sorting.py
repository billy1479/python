list1 = [34,56,34,26,80,57,98,100,80,64,102,300,35,6,87,88]
count = 0
for x in range(0,len(list1)):
    if list1[x] >= 80 and list1[x] <=100:
        print(list1[x])
        count = count + 1
print("integers in list are " + str(count))
values = []
for i in range(0, len(list1)):
    if list1[i] >= 80 and list1[i] <=100:
        values.append(list1[i])
print("")
for y in range(0, len(values)):
    try:
        print(values[y])
        list1.remove(values[y])
    except ValueError:
        pass
print(list1)
    
