# pseudo code

# prompt the user the question - what is their favorite animal?
# gather input from the user, save it to a variable
# if that value is capybara, we print out an approving message
# if value is not capybara, we print something else
# end the code


# First Approach

# print("What is your favorite animal?")
# input_animal = input()
# print(input_animal)

#Second Approach

print("What is your favorite animal?")
input_animal = input()

if input_animal == "capybara":
    print("This is my favorite animaHol too!")
else:
    if input_animal == "hedgehog":
        print("Hedgehogs too are great!")
    else:
        print("Awwwnnn, that is soo cute!")

# Now using elif statement
print("What is your favorite animal?")
input_animal = input()

if input_animal == "capybara":
    print("This is my favorite animaHol too!")
elif input_animal == "hedgehog":
    print("Hedgehogs too are great!")
else:
    print("Awwwnnn, that is soo cute!")