def my_range(*args):
    if len(args) == 2:
        start = args[0]
        end = args[1]
        step = 1
    else:
        start = args[0]
        end = args[1]
        step = args[2]
    while True:
        if  start >= end:
            break

        yield start

        start = start + step
print("range with out any steps")
for i in my_range(0,5):
    print(i)    
print("range with step increments ")
for i in my_range(0,5,2):
    print(i)