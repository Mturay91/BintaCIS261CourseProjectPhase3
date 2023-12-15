import hashlib 

#This is the function for the login

def loggin_in():
    username = input("Enter username:")
    username1 = "admin"
    password = input("Enter password: ")
    authentication = password.encode()

    #This will decrypt nto the MD5
    auth_hash = hashli.MD5(authentication).hexdigest()

    #This will read password in the text file name credentials.txt
    with open ("credentials.txt", "r") as f:
        stored_username, stored_pwd = f.read().split("\n")
    f.close()

    # This is the if statement

    if username1 == stored_username and auth_hash == stored_pwd:
        file1 = open("credentials.txt", "r+")
        print(file1.read())

    if username == stored_username and auth_hash == stored_pwd:
        print("Logged in Successfully!")
    else:
        print("Login failed! \n")

#This is the function for signing up

def signing_up():
    username = input("Enter username: ")
    password =input("Enter password: ")
    confirm_password = input("Confirm password: ")

    #Statement to confirm password
    if confirm_password == password: 
        enc = confirm_password.encode()
        hash1 = hashlib.md5(enc).hesdigest()
        with open ("credentials.txt", "w") as f: 
            f.write(username + "\n")
            f.write(hash1)
        f.close()
        print("You have  registered successfully!")
    else:
        print("Password is not same as above! \n")


#Main function that will display the menu
def main():
    while 1:
        print("------Login System----")
        print("      1. Signup")
        print("      2. Login")
        print("      3.Exit")

        #This will ask for the choice
        choice = int(input("Enter your choice: "))
        if choice == 1: 
            signing_up()
        elif choice == 2:
            loggin_in()
        elif choice == 3:
            break
        else:
            print("Wrong Choice!")
main()