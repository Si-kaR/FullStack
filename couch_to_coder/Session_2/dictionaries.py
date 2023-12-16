# Working with dictionaries
student = {
    "first_name": "Ghandi",
    "last_name": "McKing",
    "subject": "Finance",
    "result": 81,
    "contact_details": {
        "email": "dandy@example.com",
        "phone": "2334568202943"
    }
}
#Display everything in the dictitonary
print("\n",student,"\n")

#Display specific content from Dictionary
print(student["contact_details"],"\n")

#Display Name | Grades
print("\n",student["first_name"],"\n") 

#Display add stuff to Dictionary
student["date_of_birth"] = "2023/04,31"
print(student["date_of_birth"])

#Checking if something exists in Dictionary
print("middle_name" in student)


#Displaying all the keys in the dictionary
print(student.keys())

#Display all the key values in the dictionary
print("\n",student.values(),"\n")

#Get the phone number only printed out.
# print("\n\n",contact_details["phone"])






#get the phone number only printed out.
#Get the phone number out of the contact_details dictionary 
#   exiting in the student Dictionary

print("\n\n",student["contact_details"]["phone"])