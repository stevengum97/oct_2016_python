import random

def rannumber():
    values=[]
    for count in range (0,100):
        values.append(random.randint(1,10000))
    return values
values=rannumber()



def selection_sort(values):
    print values
    temp=0
    min_index=0
    count=len(values)
    for index in range (0,len(values)):
        count-=1
        min_index = values.index(min(values[index:]))
        temp= min(values[index:])
        values[min_index]=values[index]
        values[index]=temp
    print values




selection_sort(values)
