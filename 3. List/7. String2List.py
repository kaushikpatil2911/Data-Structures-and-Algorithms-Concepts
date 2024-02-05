a = 'spam'
b = list(a)
print(b)

a = 'spam spam spam'
b = a.split()
print(b)

a = 'spam-spam1-spam2'
b = a.split('-')
print(b)
delimeter = ' '
print(delimeter.join(b))