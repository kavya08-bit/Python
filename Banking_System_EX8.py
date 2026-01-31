def show_balance(balance):
        print("************************")
        print(f"Your balance is {balance:.2f}")
        print("************************")

def deposit():
    amount = float(input("Enter the amount you want to deposit: "))

    if amount < 0:
        print ("not valid input")
        return 0
    else:
        return amount

def withdraw(balance):
        amount = float(input("Enter the amount you want to withdraw: "))
        if amount > balance:
            print("insufficient money")
            return 0
        elif amount < 0:
            print("Invalid")
            return 0
        else:
            return amount


def main():
    balance =0
    is_running = True

    while is_running:
        print("************************")
        print("     Banking System     ")
        print("************************")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.withdraw")
        print("4.Exit")
        print("************************")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice =='3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("************************")
            print("Not valid input try again")
            print("************************")


    print("Thank you! Have a nice day")


if __name__ == '__main__':
    main()
