from array import *

days = int(input("How many day's temperature : "))
temperature = []
count = 1
for i in range(1,days+1):
    x = int(input(f"Day {count}'s high temperature : "))
    temperature.insert(count-1, x)
    count = count + 1
Average = sum(temperature)/len(temperature) 
print("Average : "+str(Average))

above =0
for i in temperature:
    if i<Average:
        above = above + 1
print(str(above)+" day(s) above average")        