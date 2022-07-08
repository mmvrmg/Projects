def printeven(list):
    i = 0
    evennumbers = []
    for i in range(len(list)-1):
        if list[i] % 2 == 0:
            evennumbers.append(list[i])
            i += 1

    print(evennumbers)

listofnum = [233,4,56,77,121,90,111]

printeven(listofnum)
