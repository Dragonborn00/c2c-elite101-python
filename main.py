def get_user_name():
    return input("Please enter your name: ")

def greet_user(name):
    print(f"Hello, {name}!")

def get_user_age(name):
    return input(f"Okay {name}, now I will need your age since some of the items on the menu might be age restricted ")

def main ():
    user_name = get_user_name()
    greet_user(user_name)
    user_age = get_user_age(user_name)

    print ("\nWhat can i get for you today? Please choose an option below")
    print ("1. Order food")
    print ("2. Track Your Delivery")
    print ("3. Speak to support")
    print ("4. Exit")

    while True:
        choice = input("Enter the number of your choice: ")


        if choice == "1":
            print ("Great! What would you like to order?")
            break
        elif choice == "2":
            print ("Tracking your delivery...")
            break
        elif choice == "3":
            print ("connecting you to support")
            break
        elif choice == "4":
            print ("Thanks for stopping by hope to see you again soon!")
            break
        else:
            print("Uh Oh! that doesn't seem to be a valid option. Please try again")

if __name__ == "__main__":
    print("Hi, and welcome to Bitebot. I'm here to get rid of those cravings, so tell me what you want and, you can leave the rest to me!")
    main()
