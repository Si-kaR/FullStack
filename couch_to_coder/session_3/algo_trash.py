# Algorithm is a set of instrcutions for solving a problem
# So a step - by - step procedure to solve a problem, or accomplish a task. 





#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
#                           Solving previous code
#                 
# pin = 1234
# balance = 50000


# input_pin = input("\nPlease enter your PIN number!")

# if(pin == int(input_pin)):
#     print("\nYour balance is " + str(balance))
# else:
#     print("\nIncorrect PIN! Please try again!")
#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░


# #            Iteration 1 : The code should give the User Trials (3) to get the pin right
# pin = 1234
# balance = 50000
# number_of_trial = 0

# while number_of_trial < 3:

#     input_pin = input("\nPlease enter your PIN number!")

#     if(pin == int(input_pin)):
#         print("\nYour balance is " + str(balance))
#         number_of_trial += 1
#     else:
#         print("\nIncorrect PIN! Please try again!")
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# The problem here is that  even though when the PIN is Correct 
# on the first attempt and the balance printed, the program goes back to ask the 
# User for PIN, even though. 

#SO yes, when it is wrong, it asks for PIN, but it shouldn't ask when it is right.
#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░


#        Iteration 2 : The code should give the User Trials (3) to get the pin right
#                      But should not keep asking the User when any attempt is correct
# pin = 1234
# balance = 50000
# number_of_trial = 0

# while number_of_trial < 3:

#     input_pin = input("\nPlease enter your PIN number!")

#     if(pin == int(input_pin)):
#         print("\nYour balance is " + str(balance))
#         break
#     else:
#         print("\nIncorrect PIN! Please try again!")
# SO in the second solution, I've changed from using an INCREMENT to using a BREAK
# Works now 
#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░


#        Iteration 2 : The code should give the User Trials (3) to get the pin right
#                      But should not keep asking the User when any attempt is correct
#                      Now, Check if User Entry is INT. 
#                      If not, Inform them to use an INT

#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
#        Iteration  2a : 
pin = 1234
balance = 50000
number_of_trial = 0

input_pin = input("\nPlease enter your PIN number!")


while (number_of_trial < 3):

    if( not input_pin.isdigit()):
        print("\nA PIN is a four-digit number\nPlease enter a valid PIN:\n")
    break

    if(pin == int(input_pin)): #  & input_pin.isdigit()
        print("\nYour balance is " + str(balance))
        break
    else:
        # print("\nA PIN is a four-digit number\nPlease enter a valid PIN:\n")
        print("\nIncorrect PIN! Please try again!\n")
        number_of_trial += 1
# Now what happens with this code is that, when I type anything none numeric, it does what I want it to do, 
# however, the loop breaks.. . . . 

# Soo stop the loop from breaking.
#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
#          iteration 2b:
pin = 1234
balance = 50000
number_of_trial = 0

input_pin = input("\n░░░░░░░░░░░░░░░░░░Please enter your PIN number!\n")


while (number_of_trial < 3):

    if( not input_pin.isdigit()):
        print("\nA PIN is a four-digit number\nPlease enter a valid PIN:\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
        break
    if(pin == int(input_pin)): #  & input_pin.isdigit()
        print("\nYour balance is " + str(balance))
        break
    else:
        # print("\nA PIN is a four-digit number\nPlease enter a valid PIN:\n")
        print("\nIncorrect PIN! Please try again!\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
        number_of_trial += 1

#  Still need to iterate the program however I have an asisgnment to submit so I'm just going to move on in this life I'm in 

#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░


# text = "12345"

# if text.isdigit():
#     print("All charaters in the text are numeric!")
# else:
#     print("There are non-numeric characters in the text.")







# pin = 1234
# balance = 50000
# number_of_tries = 3
# input_pin = input("Please enter your PIN number!")
# while(number_of_tries > 0):
# # .isdigit() checks if a string is valid as an int
# # not turns the conditional check to the oppositne. .isdigit() would return true
#     if(not input_pin.isdigit()):
#         print("Please enter a valid PIN number")
#     break
#     if(pin == int(input_pin)):
#         print("Your balance is " + str(balance))
#         break # ADDED
#     else:
#         input_pin = input("Incorrect PIN! Please try again!")
#         number_of_tries -= 1


























#                                Good Process for Algorithmic problem Solving
#
#
#                         1. RED - GREEN - REFACTOR
#   RED - Problem being presented and not solved
#   GREEN - Fact that code was written to solve the problem.
#   REFACTOR - The most important steps
#   
