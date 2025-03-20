#Implement a program that starts by asking the user to enter a login id (i.e., a string). The
#program then checks whether the id entered by the user is in the list ['Ahmad', 'Zainab',
#'Hina', 'Ali'] of valid users. Depending on the outcome, an appropriate message should be
#printed. Regardless of the outcome, your function should print “Done” before terminating.
#Here is an example of a successful login:
#>>>
#Login: Ali
#You are in!
#Done.
def check_login():
    """Check if the user login ID is valid."""
    valid_users = ['Ahmad', 'Zainab', 'Hina', 'Ali']  # List of valid users
    
    # Ask for login ID
    login_id = input("Login: ")
    
    # Check if login ID is valid
    if login_id in valid_users:
        print("You are in!")
    else:
        print("Access denied!")

    # Print Done before exiting
    print("Done.")

# Call the function
check_login()
