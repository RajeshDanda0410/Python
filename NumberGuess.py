#Taking username
name = input('Hi, what is your Name: ')

print('Hello ' + name + " Let's play a game!" )

#Initializing variables

count = 0; maximum = 100; minimum = 0; guess = 60

print("Think of random number from 1 to 100, and I'll try to guess it!")

# conditional statments:using (while true) for iterations 

while 1 :

    count += 1

    answer = input('is ur num ' + str(guess) + '(yes/no): ')

    if answer == "no":  # condition  for wrong guess

        secondAnswer = input('is your number larger than '+ str(guess) +'(yes/no): ')
        
        #conditions for checking number grater or lesser than guess

        if secondAnswer == 'yes':  

            minimum = guess

            guess = (maximum + guess)//2  # changing guess value if it is greater than the previous   

        elif secondAnswer == 'no':

            maximum = guess

            guess = (minimum + guess)//2   # changing guess value if it is less than the previous    

    elif answer == "yes":   # condition  for correct guess

        print('Yay!! I guessed it in '+ str(count) +' attempts') 

        nextGame = input('Do you want to play more(yes/no)?')

        if nextGame == 'yes':   # condition for playing another game

            count = 0; maximum = 100; minimum = 0; guess=60    # changing variables to initiale vlaues 

            print("Think of random number from 1 to 100, and I'll try to guess it!")

        else:

            print('Bye-bye')

            break

