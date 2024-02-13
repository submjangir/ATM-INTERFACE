class Transaction:
    def __init__(self, amount):
        self.amount = amount

    def execute(self):
        pass


class Withdrawal(Transaction):
    def execute(self):
        print(f"Withdrawing ${self.amount}")


class Deposit(Transaction):
    def execute(self):
        print(f"Depositing ${self.amount}")


class Transfer(Transaction):
    def __init__(self, amount, recipient):
        super().__init__(amount)
        self.recipient = recipient

    def execute(self):
        print(f"Transferring ${self.amount} to {self.recipient}")


class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin

    def authenticate(self, entered_pin):
        return self.pin == entered_pin


class ATM:
    def __init__(self, user):
        self.user = user

    def start(self):
        user_id = input("Enter user ID: ")
        pin = input("Enter PIN: ")

        if self.user.authenticate(pin):
            self.show_menu()
        else:
            print("Invalid credentials. Exiting...")
            return

    def show_menu(self):
        while True:
            print("\nATM Menu:")
            print("1. Transactions History")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transfer")
            print("5. Quit")

            choice = input("Enter choice: ")

            if choice == '1':
                self.show_transaction_history()
            elif choice == '2':
                self.withdraw()
            elif choice == '3':
                self.deposit()
            elif choice == '4':
                self.transfer()
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def show_transaction_history(self):
        print("Transaction History:")
        # Code to display transaction history

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        withdrawal = Withdrawal(amount)
        withdrawal.execute()

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        deposit = Deposit(amount)
        deposit.execute()

    def transfer(self):
        amount = float(input("Enter amount to transfer: "))
        recipient = input("Enter recipient's user ID: ")
        transfer = Transfer(amount, recipient)
        transfer.execute()


# Example usage:
user = User("123456", "7890")  # Replace with actual user ID and PIN
atm = ATM(user)
atm.start()