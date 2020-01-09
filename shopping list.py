list1 = ["eggs", "apple", "banana", "ham", "juice", "bread"]
list2 = ["ham", "grapes", "yoghurt", "wine", "beer", "steak"]
missing_element = []
new = []

def length(list1, list2):
    if len(list1) > len(list2):
        mainlength = len(list1)
    elif len(list2) > len(list1):
        mainlength = len(list2)
    else:
        mainlength = len(list1)
    return mainlength

def compare(list1, list2):
    for i in range(mainlength):
        for x in range(mainlength):
            if list1[i] == list2[x]:
                missing_element.append(list1[i])
                list2[x] = "R"
                list1[i] = "R"

def appending(list1, list2):
    c = mainlength
    for i in range(c):
        if list1[i] != "R":
            new.append(list1[i])
        if list2[i] != "R":
            new.append(list2[i])
    for x in range(c):
        new.append(list2[x])
    for y in range(len(missing_element)):
        new.append(missing_element)
    return new
            









mainlength = length(list1, list2)
compare(list1, list2)
for y in range(mainlength):
    if list1[y] == "R":
        pass
    else:
        print(list1[y])
    if list2[y] == "R":
        pass
    else:
        print(list2[y])
print(appending(list1,list2))
        
        
