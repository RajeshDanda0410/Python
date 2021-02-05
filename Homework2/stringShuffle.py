#initializing string
string = "codeleet"
#initializing indices
indices = [4,5,6,7,0,2,1,3]

t = list(string)  #taking a temporary variable and assgining list of string

# using for loop for shuffling string
for i in range(len(indices)):

    t[indices[i]] = string[i]

print("".join(t)) # joining string and printing
