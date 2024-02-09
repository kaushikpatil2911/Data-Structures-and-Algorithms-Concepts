
def count_word_frequency(words):
    mydict = {}
    a,o,b=0,0,0
    for item in words:
        if item == 'apple':
            a += 1
            mydict['apple'] = a
        elif item == 'orange':
            o += 1
            mydict['orange'] = o
        elif item == 'banana':
            b += 1
            mydict['banana'] = b
    print(mydict)

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
count_word_frequency(words)    