"""
An object oriented program that simulates a bank account system.
it contains functionalities such as;
withdrwal from accoount, deposit into account
and checking of balance
"""

class Bank_Account:
    """ The class is used to carry
    withdrawal, deposit and for
    checking balance of class instances.
    """
    def __init__(self, account_number = 444000, account_holder_name = "Paul White", balance = 500000): #The constructor for the class initialised to default values
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def withdrawal(self):                                       #method used to withdraw from account balance
        Acc_No = int(input("Enter your account number: "))
        if Acc_No == self.account_number:
            print("Welcome", self.account_holder_name)
        else:
            print("Please enter a valid account number: ")
        With_amt = int(input("Enter amount to withdraw: "))
        if With_amt > self.balance:
            print("your account balance is insufficient for this transaction")

        else:
            self.__balance = self.balance - With_amt
            print("your wihdrawal of {} is successful".format(With_amt))
            return self.__balance                           #returns encapsulated __balance


    def deposit(self):                                   #metthod for depositing into account by adding to the balance
        Acc_No = int(input("please enter account number you wish to deposit into: "))
        if Acc_No != self.account_number:
            print("enter a valid account number")
        else:
            deposit_amt = int(input("please enter amount you wish to deposit: "))
            self.__balance = self.balance + deposit_amt
            return self.__balance                       #returns encapsulated and modified balance

    def check_balance(self):
        try:
            Acc_no = int(input("Enter account number to check balance: "))
            if Acc_no != self.account_number:
                print("Incorrect account number")
            else:
                print("your account balance is: {}".format(self.__balance))
        except Exception:                                                          #try and except block is used here
            print("your account balance is {}: ".format(self.balance))          #to catch exceptions that result from
                                                                            #returning a balance lower than self.balance
                                                                                        #after a withdrawal attempt





customer_Tony = Bank_Account(444000, "Tony Paul", 500000)        #class instance created and initialised with variables
                                                                #for account number, name and account balance


customer_Tony.withdrawal()                              #withdrawal method is called to carry out withdrawal on the customer instance
customer_Tony.check_balance()                           #to check balance after withdrawal from the customer's account
















