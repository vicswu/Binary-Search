'''
Victor Wu
Tuesday , February 19th
'''

#Exercise
hi=101 #Define the upper limit of the range. 
lo=1#Define the lower limit of the range. 
print("Please think of a number between 1 and 100.")
while input!="c":
    guess = (hi+lo) // 2
    print("Is your secret number", guess, "?")
    answer = input("Enter ’h’ if my guess is too high, ’l’ if too low, or ’c’ if I am correct:")
    if answer == 'h' :
        hi = guess
    elif answer == 'l' :
        lo = guess
    elif answer == 'c':
        break      #Ends look if the answer is c. Found right number.
    else:          #Handles cases where the input is not c,h or l. Forces the user to enter the correct letter. 
        print('Sorry, I did not understand your input.')
print("Game over. Your secret number was:", guess)
