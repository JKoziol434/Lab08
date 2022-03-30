#Username request
userName = input("Hello! Please enter your facebook username! ")

#Password request
userPassword = input("Hello! Please enter your facebook password! ")

#If statement for credentials
if(userName.lower() == "joshua" and userPassword == "Rhody!"):
    print("Welcome to facebook!")
else:
    print("Wrong credentials, try again!")
