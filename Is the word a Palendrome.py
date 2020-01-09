t = 0
while t == 0:
    mode = str(input('Enter the mode you want to do : '))
    if mode=='play':
        word = str(input("Enter the word you want to test : "))
        length = len(word)
        stack = [' '] * length
        head = 0

        array = [' '] * length
        counter = 0
        for i in range(length-1, -1, -1):
            stack[counter] = word[i]
            counter = counter + 1

        c = 0
        for x in range(length-1):
            if stack[x] == word[x]:
                c = c + 1
                
        if c == length - 1:
            print("The word is a palendrome")
        else:
            print("The word is not a palendrome")
    else:
        t = 1
        print("Game Over")

        
