'''
 program with counter 

from collections import Counter


mylist=["one", "two","eleven",  "one", "three", "two", "eleven", "three", "seven", "eleven"]

def count_frequency(z):
    c = Counter(z)
    return c
print(count_frequency(mylist))'''

mylist=["one", "two","eleven",  "one", "three", "two", "eleven", "three", "seven", "eleven"]
def count_frequency(z):
    frequent = {} 
    for item in z: 
        if (item in frequent): 
            frequent[item] += 1
        else: 
            frequent[item] = 1
    return frequent
print(count_frequency(mylist))