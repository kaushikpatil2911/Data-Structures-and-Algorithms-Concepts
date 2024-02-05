myList = []
while(True):
    inp = input("Enter the number : ")
    if inp == 'done':
        break
    value = float(inp)
    myList.append(value)
print("Average : ",sum(myList)/len(myList))