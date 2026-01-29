# ATM Simulation Program
# This program allows a user to check balance, deposit money, and withdraw money

# Initial balance in the ATM account
balance = 5000


# Function to display ATM menu
def show_menu():
    print("\n----- ATM MENU -----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")


# ATM runs continuously until user chooses to exit
while True:
    show_menu()  # Display menu options

    # Taking user choice
    choice = int(input("Enter your choice (1-4): "))

    # Option 1: Check Balance
    if choice == 1:
        print("Your current balance is:", balance)

    # Option 2: Deposit Money
    elif choice == 2:
        deposit = int(input("Enter amount to deposit: "))

        if deposit > 0:
            balance += deposit
            print("Deposit successful!")
            print("Updated balance:", balance)
        else:
            print("Invalid deposit amount")

    # Option 3: Withdraw Money
    elif choice == 3:
        withdraw = int(input("Enter amount to withdraw: "))

        if withdraw > balance:
            print("Insufficient balance!")
        elif withdraw <= 0:
            print("Invalid withdrawal amount")
        else:
            balance -= withdraw
            print("Please collect your cash")
            print("Remaining balance:", balance)

    # Option 4: Exit
    elif choice == 4:
        print("Thank you for using the ATM. Goodbye!")
        break  # Exit the loop

    # Invalid choice
    else:
        print("Invalid choice. Please try again.")






