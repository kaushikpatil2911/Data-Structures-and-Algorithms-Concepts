a = [1,2,3]
b = [4,5,6]

c =a+b
print(c)

c =a*4
print(c)

a = [1,2,3,4,5,6,7,8,9]
print(len(a))

a = [1,2,3,4,5,6,7,8,9]
print(max(a))

a = [1,2,3,4,5,6,7,8,9]
print(min(a))

a = [1,2,3,4,5,6,7,8,9]
print(sum(a))

a = [1,2,3,4,5,6,7,8,9]
print(sum(a)/len(a)) #Average

#Average of list elements
myList = []
while(True):
    inp = input("Enter the number (done to finish) : ")
    if inp == 'done' and len(myList) > 0:
        break
    value = float(inp)
    myList.append(value)
print("Average : ",sum(myList)/len(myList))

