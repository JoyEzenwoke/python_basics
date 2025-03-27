age = int(input("enter your age :"))
nationality = input("enter your nationality :")
if age >= 18 and nationality == "nigerian":
 print("you are eligable to vote in Nigeria.")
elif age < 18 and nationality == "nigerian":
 print("You are too young to vote.")
else:
 print("You must be a Nigerian citizen to vote here.")

