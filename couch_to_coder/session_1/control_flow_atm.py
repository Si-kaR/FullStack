# 1. Create a file called control_flow_atm.py
# 2. Create a variable called balance with an int value representing the money in the user's account

# 3. Create a variable called pin with an int value (for example 1234)
# 4. Prompt the user to enter their pin!

# 5. If the pin values match, display their balance.
# 6. If they don't match, print out a message notifying the user.

# Extensions:
# 7. If the pin matches, give the prompt to the user if they'd like to withdraw or deposit some money.
# 8. Once they made their choice, prompt them to enter an amount.
# 9. Subtract or add the value to their account balance, then display the updated balance!





#This is balance of user
balance = 0
# This is the pin
pin = 9381
# Prommpting user to enter pin
prompt = int(input("\nEnter your pin: \n"))
# checking if provided pin matches saved pin
if prompt == pin:
    print("\nBalance: $", balance)
else:
    print("\nincorrect pin!")



























# # Applying Extensions
# # This is balance of user
# balance = 0
# # This is the pin
# pin = 9381
# # Prommpting user to enter pin
# prompt = int(input("\nEnter your pin: \n"))
# # checking if provided pin matches saved pin
# if prompt == pin:
#     print("\nBalance: $", balance)
#     # Prompting user for transfer (withdrawal or deposit) request 
#     transfer = str(input("\nWill you like to make a withdrawal or deposit?\nEnter WITHDRAW or DEPOSIT: | | | | | ").upper())
#     #
#     #
#     if transfer == "withdraw".upper():
#         #Asking amount to withdraw
#         withdraw = int(input("\nAmount to withdraw:\n$"))
#         #Creating condition to ensure amount in account can actually be withdrawn
#         if (withdraw >= 0) or (balance - withdraw == -balance):
#             print("\nSorry, young one!\nYou have insufficient funds in your account to complete this transaction.")
#         else:
#             if (balance > withdraw) and (balance - withdraw != -balance):
#                 balance -= withdraw
#                 print("Loading . . . \n")
#                 print("Amount withdrawn: $", withdraw, "\nCurrent Balance: $", balance)
#     else:
#         if transfer == "deposit".upper():
#         #Asking amount to be deposited
#             deposit = int(input("Amount to deposit:\n$"))
#             balance += deposit
#             print("Loading . . . \n")
#             print("Amount deposit: $", deposit, "\nCurrent Balance: $", balance)

# else:
#     print("incorrect pin!")







# Applying Extensions
# This is balance of user
balance = 0
# This is the pin
pin = 9381
# Prommpting user to enter pin
prompt = int(input("\nEnter your pin: \n"))
# checking if provided pin matches saved pin
while prompt == pin:
    print("\nBalance: $", balance)
    # Prompting user for transfer (withdrawal or deposit) request 
    transfer = str(input("\nWill you like to make a withdrawal or deposit?\nEnter WITHDRAW or DEPOSIT: | | | | | ").upper())
    #
    #
    if transfer == "withdraw".upper():
        #Asking amount to withdraw
        withdraw = int(input("\nAmount to withdraw:\n$"))
        #Creating condition to ensure amount in account can actually be withdrawn
        if (withdraw >= 0) or (balance - withdraw == -balance):
            print("\nSorry, young one!\nYou have insufficient funds in your account to complete this transaction.")
            print("Would you like to make a deposit? Enter YES or NO")
        else:
            if (balance > withdraw) and (balance - withdraw != -balance):
                balance -= withdraw
                print("Loading . . . \n")
                print("Amount withdrawn: $", withdraw, "\nCurrent Balance: $", balance)
    else:
        if transfer == "deposit".upper():
        #Asking amount to be deposited
            deposit = int(input("Amount to deposit:\n$"))
            balance += deposit
            print("Loading . . . \n")
            print("Amount deposit: $", deposit, "\nCurrent Balance: $", balance)

    
else:
    print("incorrect pin!")

