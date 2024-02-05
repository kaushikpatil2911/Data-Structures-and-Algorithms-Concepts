myList = [1,2,3,4,5,6,7,8,9]
newList = [i*2 for i in myList]
print(myList)
print(newList)

language = "Python"
newList = [letter for letter in language]
print(newList)

myList = [1,-2,-3,4,5,6,-7,8,-9]
newList = [number for number in myList if number>0]
print(newList)

myList = [1,-2,-3,4,5,6,-7,8,-9]
newList = [number**2 for number in myList if number<0]
print(newList)

sentence = 'My Name is Kaushik'
def isConsonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels
print(isConsonant('t'))
consonants = [i for i in sentence if isConsonant(i)]
print(consonants)

myList = [1,-2,-3,4,5,6,-7,8,-9]
newList = [number if number>0 else 0 for number in myList]
print(newList)

def getNumber(number):
    return number if number>0 else 'negative number'
newList = [getNumber(number) for number in myList]
print(newList) 