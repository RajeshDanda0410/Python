import time 

def decorator(func):
    def inside_function():
        print("the sum of elements in simple function is ")
        return func()
    return inside_function

def simple():
    a = 5
    b = 6
    print(a+b)

start = time.time()
new_function = decorator(simple)
new_function()
end = time.time()
print(end-start)