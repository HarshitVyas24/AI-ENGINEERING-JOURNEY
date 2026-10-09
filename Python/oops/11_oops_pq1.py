class InsufficientBalanceError(Exception):

    pass

class BankAccount:

    def __init__(self,account_number, owner_name, balance):

        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self , depo_amnt):

        self.depo_amnt = depo_amnt

        self.balance = self.balance + depo_amnt

        print(f"{depo_amnt} Rs. Credited to accounmt number {self.account_number}")

    def withdraw(self, withd_amnt):

        self.withd_amnt = withd_amnt

        self.balance = self.balance - withd_amnt

        if (self.balance <0):
            print("Onssufficient Balance!")
            InsufficientBalanceError(f"Insufficient Balance!")

        else:
            print(f"{withd_amnt} Rs. Debited from accounmt number {self.account_number}")

    def checkBalance(self):
        print(f"Avl. Balance = {self.balance}")


acc1 = BankAccount(23456643 , "rahul", 100)

acc1.deposit(300)

acc1.withdraw(400)

acc1.checkBalance()
        
            