import json
with open("035_signup_data.json", "r")as file:
    my_list_dict = json.load(file)
data_dict  = {
        "Id": input("Enter ID: "),
        "First_Name": input("Enter First Name: "),
        "Last_Name": input("Enter Last Name: "),
        "Email": input("Enter Email: "),
        "Password": input("Enter Password: ")
 }

my_list_dict.append(data_dict)

with open("035_signup_data.json", "w")as file:
    json.dump(my_list_dict, file, indent=4)
print("signup data added successfully!!")

