list1 = [2,5,15,36,47,56,59,78,156,244,268]
list2 = [18,39,42,43,66,69,100]
values = []
for x in range(len(list1)):
    values.append(list1[x])
for y in range(len(list2)):
    for z in range(len(values)):
        if list2[y] < values[z]:
            values.insert(z, list2[y])
            break
print(list1)
print(list2)
print(values)
