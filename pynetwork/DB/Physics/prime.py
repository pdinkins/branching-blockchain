#Prime Number Checker
#Parker Dinkins

'''
This program asks for a number between 0 and 5000
If the number isn't in that range it asks for it again
When a proper number is entered it checks if it is prime
If the numbr is prime it prints the two factors
If the number is not prime it prints all the factors
Finally it asks if you want run the checker again or not
'''


# This function takes a number and prints the factors
def print_factors(x):
    print("The factors of", x, "are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)
    print(x, "is NOT a prime number")


# this functoin check to see if a number is prime and if so prints that out
# if the numbe is not prime it pushes the user input variable into the print_factors function
def prime_checker():
    try:
        # user input
        a = int(input("Enter a number between 0 and 5000: "))

        # checks to make sure the number is within the specified range
        if a > 5000:

            # prints out and error if the check fails and reruns the  function with clean memory   
            print('\n\t****ERROR****')
            print('Enter a number between 0 and 5000\n')
            return prime_checker()

        # place hold variable 
        k = 0

        # this finds the number of factors of the number 
        for i in range(1, a):
            if a % i == 0:
                k = k + 1

        # this checks to see if the number has less than or one factor
        # if the number satisfies this then it is prime and it prints out
        if k <= 1:
            print('The factors of your number are:')
            print('1')
            print(a, 'is a prime number')

        # if the number has more than one factor it is not prime and it lands here
        # the number is then put into the print_factors function 
        else:
            print_factors(x=a)

    # this handles the error when the user inputs something other than number into the input statement
    except ValueError:
        print('\n\t****Invalid*Input****\n\tPlease enter a number\n')

# loop variables
run = True
run1 = True

# first loop that runs the functions when the program one time when the program is opened
while run1:        
    prime_checker()
    break

# second loop that asks the user if they want to run the program again or quit
while run:
    option = input("\nContinue and run again? [y/n]: ").lower()
    if option == "y":
        prime_checker()
    elif option == "n":
        break
    else:
        print("\nNot a valid option. Please enter 'y' or 'n'")
