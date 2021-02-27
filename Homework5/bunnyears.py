def bunnyEars(a):
    if a == 0:
       return 0 
    elif a % 2 == 0:
       return 3 + bunnyEars(a-1)
    else:
       return 2 + bunnyEars(a-1) 
print(bunnyEars(0))
print(bunnyEars(1))
print(bunnyEars(2))