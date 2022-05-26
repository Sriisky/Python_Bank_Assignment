# Sara Egan C20353056 TU858-2 Assignment
# 18/12/2021
# Program to run a banking management system

import os # to create files
from datetime import date, timedelta # used to help with the withdrawal cap on the savings account
import random # used to generate transaction id, acc nums etc


# Customer Superclass
class Customer (object):
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
        self.custid = random.randint(0, 999999)

    def __str__(self):
        return "{}|{}|{}".format(self.custid, self.name, self.age)

    # to add a new customer to the file
    def addCustToFile(self):
        with open("customers.txt", "a+") as fileObject:
            # Move read cursor to the start of file.
            fileObject.seek(0)
            # If file is not empty then append '\n'
            data = fileObject.read(100)
            if len(data) > 0:
                fileObject.write("\n")
            # Append text at the end of file
            fileObject.write(self.__str__())


# BankAccount Parent Class
class BankAccount (object):
    def __init__(self, name="", age=0, pin=0, accNo=0, balance=0):
        self.name = name
        self.age = age
        self.pin = pin
        self.accNo = accNo
        self.balance = balance
        self.transactionID = 0
        self.client_details_list = []
        self.transfer_list = []
        self.loggedin = False
        self.TransferCash = False
        self.convert_str = ""

    def __str__(self):
        return "{}|{}|{}|{}|{}".format(self.accNo, self.pin, self.balance, self.name, self.age)

    def formatToFile(self):
        return "{}|{}|{}|{}|{}".format(self.accNo, self.pin, self.balance, self.name, self.age)

    # to login to an already existing account
    def login(self, name="", pin=0):
        with open("accounts.txt", "r") as fileObject:
            for lines in fileObject:
                if str(name) in lines:
                    self.client_details_list = lines.split("|")
                    if str(name) == str(self.client_details_list[3]):
                        if str(pin) == str(self.client_details_list[1]):
                            # details = fileObject.read()
                            # if str(name) in str(self.client_details_list):
                            self.loggedin = True

            if self.loggedin is True:
                self.accNo = int(self.client_details_list[0])
                self.pin = self.client_details_list[1]
                self.balance = int(self.client_details_list[2])
                self.name = self.client_details_list[3]
                self.age = self.client_details_list[4]

                print("{}|{}|{}|{}|{}".format(int(self.accNo), int(self.pin), int(self.balance), self.name, self.age))
                return True

            else:
                print("Sorry, you entered in the wrong details")

    # to update the accounts file with new accounts
    def writeBankToFile(self):
        with open("accounts.txt", "a+") as fileObject:
            # used to change the position of the File Handle to a given specific position
            fileObject.seek(0)
            # appending \n to make it easier to access the data later by seperating by new lines
            data = fileObject.read(100)
            if len(data) > 0:
                fileObject.write("\n")
            # append our text to the end of the file
            fileObject.write(self.formatToFile())

        # to deposit funds to the main bank account
        def depositFunds(self, amount):
            self.balance += amount
            self.transactionID = random.randint(0, 999999)
            details = "{}|Deposited {} to account number {}. The new balance is {}".format(self.transactionID, amount,
                                                                                           self.accNo, self.balance)

            # to add the transaction that just occured to the transactions file
            with open("accountstransactions.txt", "a+") as fileObject:
                # used to change the position of the File Handle to a given specific position
                fileObject.seek(0)
                # appending \n to make it easier to access the data later by seperating by new lines
                data = fileObject.read(100)
                if len(data) > 0:
                    fileObject.write("\n")
                # Append text at the end of file
                fileObject.write(details)

            # The easiest way to update ane external file is to write the content to the temp file and simply replace the old file with the new one
            # helps with the fact when you 'w' to a file it erases the content that is in the file
            with open("accounts.txt", "r") as file_input:
                with open("temp.txt", "w") as file_output:
                    # iterate all lines from file
                    for line in file_input:
                        # if substring contain in a line then don't write it
                        if str(self.accNo) not in line.strip("\n"):
                            file_output.write(line)

            # replace file with old files name
            os.replace('temp.txt', 'accounts.txt')

            # to update the account balances in the accounts text file
            with open("accounts.txt", "a+") as fileObject:
                # used to change the position of the File Handle to a given specific position
                fileObject.seek(0)
                # appending \n to make it easier to access the data later by seperating by new lines
                data = fileObject.read(100)
                if len(data) > 0:
                    fileObject.write("\n")
                # Append text at the end of file
                fileObject.write(self.formatToFile())

    # to print the file that holds all account transactions
    def printTransactions(self):
        with open("accountstransactions.txt", "r") as fileObject:
            for line in fileObject:
                if str(self.accNo) in line:
                    print(line)
            print()

    # to check the balance of the main bank account
    def viewBalance(self):
        print("Your general account balance is {}".format(self.balance))


    # to transfer funds to different accounts
    def transferFunds(self, amount, accNo):
        if self.balance < amount:
            print("Sorry, you have insufficient funds")
        elif self.balance > amount:
            self.balance -= amount
            self.transactionID = random.randint(0, 999999)
            details = "{}|Transferred {} from account number {} to account number {}. Your balance is {}".format(self.transactionID, amount, self.accNo, accNo, self.balance)

            # Updating the transferred amount into the transactions file
            with open("accountstransactions.txt", "a+") as fileObject:
                # used to change the position of the File Handle to a given specific position
                fileObject.seek(0)
                # appending \n to make it easier to access the data later by seperating by new lines
                data = fileObject.read(100)
                if len(data) > 0:
                    fileObject.write("\n")
                # Append text at the end of file
                fileObject.write(details)

            # Updating line
            with open("accounts.txt", "r") as file_input:
                with open("temp.txt", "w") as file_output:
                    # iterate all lines from file
                    for line in file_input:
                        # if substring contain in a line then don't write it
                        if str(self.accNo) not in line.strip("\n"):
                            file_output.write(line)

            # rename the temp file accounts
            os.replace('temp.txt', 'accounts.txt')

            # apend
            with open("accounts.txt", "a+") as fileObject:
                # used to change the position of the File Handle to a given specific position
                fileObject.seek(0)
                # appending \n to make it easier to access the data later by seperating by new lines
                data = fileObject.read(100)
                if len(data) > 0:
                    fileObject.write("\n")
                # Append text at the end of file
                fileObject.write(self.formatToFile())

            with open("accounts.txt", "r") as fileObject:
                for lines in fileObject:
                    if str(accNo) in lines:
                        self.transfer_list = lines.split("|")
                        self.transfer_list[3] = int(self.transfer_list[3]) + amount
                        self.transfer_list[3] = str(self.transfer_list[3])
                        self.convert_str = '|'.join(self.transfer_list)

            # Updating Receiver Account
            # Deleting line
            with open("accounts.txt", "r") as file_input:
                with open("temp.txt", "w") as file_output:
                    # iterate all lines from file
                    for line in file_input:
                        # if substring contain in a line then don't write it
                        if str(accNo) not in line.strip("\n"):
                            file_output.write(line)

            # replace file with original name
            os.replace('temp.txt', 'accounts.txt')

            # Adding
            with open("accounts.txt", "a+") as fileObject:
                # used to change the position of the File Handle to a given specific position
                fileObject.seek(0)
                # appending \n to make it easier to access the data later by seperating by new lines
                data = fileObject.read(100)
                if len(data) > 0:
                    fileObject.write("\n")
                # Append text at the end of file
                fileObject.write(self.convert_str)

    def withdrawFunds(self, amount):
        if self.balance < amount:
            print("Sorry, insufficient funds")
        elif self.balance > amount:
            self.balance -= amount
            self.transactionID = random.randint(0, 999999)
            caller = "{}| Withdrew {} from account number {}. Your new balance is {}".format(self.transactionID, amount, self.accNo, self.balance)

            with open("accountstransactions.txt", "a+") as fileObject:
                # used to change the position of the File Handle to a given specific position
                fileObject.seek(0)
                # appending \n to make it easier to access the data later by seperating by new lines
                data = fileObject.read(100)
                if len(data) > 0:
                    fileObject.write("\n")
                # Append text at the end of file
                fileObject.write(caller)

            with open("accounts.txt", "r") as file_input:
                with open("temp.txt", "w") as file_output:
                    # iterate all lines from file
                    for line in file_input:
                        # if substring contain in a line then don't write it
                        if str(self.accNo) not in line.strip("\n"):
                            file_output.write(line)

            # replace file with original name
            os.replace('temp.txt', 'accounts.txt')

            with open("accounts.txt", "a+") as fileObject:
                # used to change the position of the File Handle to a given specific position
                fileObject.seek(0)
                # appending \n to make it easier to access the data later by seperating by new lines
                data = fileObject.read(100)
                if len(data) > 0:
                    fileObject.write("\n")
                # Append text at the end of file
                fileObject.write(self.formatToFile())

    # method delete Account
    def deleteAccount(self):
        with open("accounts.txt", "r") as file_input:
            with open("temp.txt", "w") as file_output:
                # iterate all lines from file
                for line in file_input:
                    # if substring contain in a line then don't write it
                    if str(self.accNo) not in line.strip("\n"):
                        file_output.write(line)

        # replace file with original name
        os.replace('temp.txt', 'accounts.txt')


class SavingsAccount (BankAccount):
    def __init__(self, name="", age=0, pin=0, accNo=0, balance=0, mode="Savings", withdrew_date=date.today().isoformat()):
        BankAccount.__init__(self, name, age, pin, accNo, balance)
        self.mode = mode
        self.withdrew_date = withdrew_date

    def __str__(self):
        result_str = BankAccount.__str__(self) + "|{}|{}".format(self.mode, self.withdrew_date)
        return result_str

    def initialSavings(self, amount=0):
        self.balance = amount

        with open("savingaccount.txt", "a+") as fileObject:
            # used to change the position of the File Handle to a given specific position
            fileObject.seek(0)
            # appending \n to make it easier to access the data later by seperating by new lines
            data = fileObject.read(100)
            if len(data) > 0:
                fileObject.write("\n")
            # Append text at the end of file
            fileObject.write(self.formatToFile())

    def viewBalance(self):
        print("Your savings account balance is {}".format(self.balance))

    def formatToFile(self):
        return "{}|{}|{}|{}|{}|{}|{}".format(self.accNo, self.pin, self.balance, self.name, self.age, self.mode, self.withdrew_date)

    def login(self, accNo=0, pin=0):
        with open("savingaccount.txt", "r") as fileObject:
            for lines in fileObject:
                if str(accNo) in lines:
                    self.client_details_list = lines.split("|")
                    if str(accNo) == str(self.client_details_list[0]):
                        if str(pin) == str(self.client_details_list[1]):
                            self.loggedin = True

            if self.loggedin is True:
                self.accNo = int(self.client_details_list[0])
                self.pin = int(self.client_details_list[1])
                self.balance = int(self.client_details_list[2])
                self.name = self.client_details_list[3]
                self.age = self .client_details_list[4]
                self.mode = self.client_details_list[5]
                self.withdrew_date = self.client_details_list[6]

                print("{}|{}|{}|{}|{}|{}|{}".format(int(self.accNo), self.pin, int(self.balance), self.name, self.age, self.mode, self.withdrew_date))

                return True

            else:
                print("Sorry, you entered in the wrong details")

    def depositFunds(self, amount):
        self.balance += amount
        self.transactionID = random.randint(0, 999999)
        caller = "{}|Deposited {} to savings account number {}. Your new balance is {}".format(self.transactionID, amount, self.accNo, self.balance)

        with open("accountstransactions.txt", "a+") as fileObject:
            # used to change the position of the File Handle to a given specific position
            fileObject.seek(0)
            # appending \n to make it easier to access the data later by seperating by new lines
            data = fileObject.read(100)
            if len(data) > 0:
                fileObject.write("\n")
            # Append text at the end of file
            fileObject.write(caller)

        with open("savingaccount.txt", "r") as file_input:
            with open("temp.txt", "w") as file_output:
                # iterate all lines from file
                for line in file_input:
                    # if substring contain in a line then don't write it
                    if str(self.accNo) not in line.strip("\n"):
                        file_output.write(line)

        # replace file with original name
        os.replace('temp.txt', 'savingaccount.txt')

        with open("savingacccount.txt", "a+") as fileObject:
            # used to change the position of the File Handle to a given specific position
            fileObject.seek(0)
            # appending \n to make it easier to access the data later by seperating by new lines
            data = fileObject.read(100)
            if len(data) > 0:
                fileObject.write("\n")
            # Append text at the end of file
            fileObject.write(self.formatToFile())

    def withdrawFunds(self, amount):
        if self.withdrew_date.days <= 30:
            self.balance -= amount
            self.transactionID = random.randint(0, 999999)
            caller = "{}| Withdrew {} from savings account number {}. Your new balance is {}".format(self.transactionID, amount, self.accNo, self.balance)

            with open("accountstransactions.txt", "a+") as fileObject:
                # used to change the position of the File Handle to a given specific position
                fileObject.seek(0)
                # appending \n to make it easier to access the data later by seperating by new lines
                data = fileObject.read(100)
                if len(data) > 0:
                    fileObject.write("\n")
                # Append text at the end of file
                fileObject.write(caller)

            with open("savingaccount.txt", "r") as file_input:
                with open("temp.txt", "w") as file_output:
                    # iterate all lines from file
                    for line in file_input:
                        # if substring contain in a line then don't write it
                        if str(self.accNo) not in line.strip("\n"):
                            if str(self.mode) not in line.strip("\n"):
                                file_output.write(line)

            # replace file with original name
            os.replace('temp.txt', 'savingaccount.txt')

            with open("savingaccount.txt", "a+") as fileObject:
                # used to change the position of the File Handle to a given specific position
                fileObject.seek(0)
                # appending \n to make it easier to access the data later by seperating by new lines
                data = fileObject.read(100)
                if len(data) > 0:
                    fileObject.write("\n")
                # Append text at the end of file
                fileObject.write(self.formatToFile())
        else:
            print("You have already made a withdrawal in the last month. Please wait until {} before making another".format(self.withdrew_date))

    # Only general account can perform money transfer
    def transferFunds(self, amount, accNo):
        return

    def deleteAccount(self, mode="Savings"):
        if self.balance == 0:
            caller = "{}|Deleted savings account number {} ".format(self.transactionID, self.accNo)

            with open("accountstransactions.txt", "a+") as fileObject:
                # used to change the position of the File Handle to a given specific position
                fileObject.seek(0)
                # appending \n to make it easier to access the data later by seperating by new lines
                data = fileObject.read(100)
                if len(data) > 0:
                    fileObject.write("\n")
                # Append text at the end of file
                fileObject.write(caller)

                with open("savingaccount.txt", "r") as file_input:
                    with open("temp.txt", "w") as file_output:
                        # iterate all lines from file
                        for line in file_input:
                            # if substring contain in a line then don't write it
                            if str(self.mode) not in line.strip("\n"):
                                file_output.write(line)

            # replace file with original name
            os.replace('temp.txt', 'savingaccount.txt')

        else:
            print("Unable to delete account")

def formatAttributes(accNo):
    details = []
    with open("accounts.txt", "r") as fileObject:
        for lines in fileObject:
            if str(accNo) in lines:
                list = lines.split("|")

                for el in list:
                    details.append(el.strip())
                details[2] = 0
                print(details)
    return details

class CheckingAccount (BankAccount):
    def __init__(self, name="", age=0, pin=0, accNo=0, balance=0, mode="Checking"):
        BankAccount.__init__(self, name, age, pin, accNo, balance)
        self.mode = mode

    def __str__(self):
        result_str = BankAccount.__str__(self) + "|{}".format(self.mode)
        return result_str

    def initialCheckingBal(self, amount=0):
        self.balance = amount

        with open("checkingaccount.txt", "a+") as fileObject:
            # used to change the position of the File Handle to a given specific position
            fileObject.seek(0)
            # appending \n to make it easier to access the data later by seperating by new lines
            data = fileObject.read(100)
            if len(data) > 0:
                fileObject.write("\n")
            # Append text at the end of file
            fileObject.write(self.formatToFile())

    def viewBalance(self):
        print("Your checking account balance is {}".format(self.balance))

    def formatToFile(self):
        return "{}|{}|{}|{}|{}|{}".format(self.accNo, self.pin, self.balance, self.name, self.age, self.mode)

    def depositFunds(self, amount):
        self.balance += amount
        self.transaction_id = random.randint(0, 999999)
        caller = "{}|Deposited {} to checking account number {}. Your new balance is {}".format(self.transaction_id, amount, self.accNo, self.balance)

        with open("accountstransactions.txt", "a+") as fileObject:
            # used to change the position of the File Handle to a given specific position
            fileObject.seek(0)
            # appending \n to make it easier to access the data later by seperating by new lines
            data = fileObject.read(100)
            if len(data) > 0:
                fileObject.write("\n")
            # Append text at the end of file
            fileObject.write(caller)

        with open("checkingaccount.txt", "r") as file_input:
            with open("temp.txt", "w") as file_output:
                # iterate all lines from file
                for line in file_input:
                    # if substring contain in a line then don't write it
                    if str(self.accNo) not in line.strip("\n"):
                        file_output.write(line)

        # replace file with original name
        os.replace('temp.txt', 'checkingaccount.txt')

        with open("checkingaccount.txt", "a+") as fileObject:
            # Move read cursor to the start of file.
            fileObject.seek(0)
            # If file is not empty then append '\n'
            data = fileObject.read(100)
            if len(data) > 0:
                fileObject.write("\n")
            # Append text at the end of file
            fileObject.write(self.formatToFile())

    def withdrawFunds(self, amount):
        self.balance -= amount
        self.transaction_id = random.randint(0, 999999)
        caller = "{}| Withdrew {} from checking account number {}. Your new balance is {}".format(self.transaction_id, amount, self.accNo, self.balance)

        with open("accountstransactions.txt", "a+") as fileObject:
            # used to change the position of the File Handle to a given specific position
            fileObject.seek(0)
            # appending \n to make it easier to access the data later by seperating by new lines
            data = fileObject.read(100)
            if len(data) > 0:
                fileObject.write("\n")
            # Append text at the end of file
            fileObject.write(caller)

        with open("checkingaccount.txt", "r") as file_input:
            with open("temp.txt", "w") as file_output:
                # iterate all lines from file
                for line in file_input:
                    # if substring contain in a line then don't write it
                    if str(self.accNo) not in line.strip("\n"):
                        if str(self.mode) not in line.strip("\n"):
                            file_output.write(line)

        # replace file with the original name
        os.replace('temp.txt', 'checkingaccount.txt')

        with open("checkingaccount.txt", "a+") as fileObject:
            # used to change the position of the File Handle to a given specific position
            fileObject.seek(0)
            # appending \n to make it easier to access the data later by seperating by new lines
            data = fileObject.read(100)
            if len(data) > 0:
                fileObject.write("\n")
            # Append text at the end of file
            fileObject.write(self.formatToFile())

    def login(self, accNo=0, pin=0):
        with open("checkingaccount.txt", "r") as fileObject:
            for lines in fileObject:
                if str(accNo) in lines:
                    self.client_details_list = lines.split("|")
                    if str(accNo) == str(self.client_details_list[0]):
                        if str(pin) == str(self.client_details_list[1]):
                            # details = file_object.read()
                            # if str(name) in str(self.client_details_list):
                            self.loggedin = True

            if self.loggedin is True:
                self.accNo = int(self.client_details_list[0])
                self.pin = self.client_details_list[1]
                self.balance = int(self.client_details_list[2])
                self.name = self.client_details_list[3]
                self.age = self .client_details_list[4]
                self.mode = self.client_details_list[5]

                print("{}|{}|{}|{}|{}|{}".format(int(self.accNo), self.pin, int(self.balance), self.name, self.age, self.mode))

                return True

            else:
                print("Wrong details")

    def transferFunds(self, amount, acc_no):
        return

    def deleteAccount(self, mode="Checking"):
        if self.balance == 0:
            details = "{}|Deleted checking account number {} ".format(self.transaction_id, self.accNo)

            with open("accountstransactions.txt", "a+") as fileObject:
                # used to change the position of the File Handle to a given specific position
                fileObject.seek(0)
                # appending \n to make it easier to access the data later by seperating by new lines
                data = fileObject.read(100)
                if len(data) > 0:
                    fileObject.write("\n")
                # Append text at the end of file
                fileObject.write(details)

                with open("checkingaccount.txt", "r") as file_input:
                    with open("temp.txt", "w") as file_output:
                        # iterate all lines from file
                        for line in file_input:
                            # if substring contain in a line then don't write it
                            if str(self.mode) not in line.strip("\n"):
                                file_output.write(line)

            # replace file with original name
            os.replace('temp.txt', 'checkingaccount.txt')

        else:
            print("Unable to delete account")

def main():
    bank_object = BankAccount()
    print("Sara's Banking Management System")
    print("-----------------")
    print("(1) Login to my account")
    print("(2) Create a new account")
    print("-----------------")
    try:
        while True:
            print("-----------------")
            option = int(input("Select an option: "))
            print("-----------------")
            if option == 1:
                name = input("\nEnter your full name: ")

                pin = int(input("Enter your pin: "))

                result = bank_object.login(name, pin)

                if result is True:
                    try:
                        while True:
                            # Printing menu
                            print("\nSara's Banking Management System")
                            print("-----------------")
                            print("(1) Create a new account")
                            print("(2) View transactions")
                            print("(3) Account services")
                            print("(4) Delete an account")
                            print("(5) Exit")
                            print("-----------------\n")
                            selection2 = int(input("Please enter your selection: "))
                            if selection2 == 1:
                                print("Please select what type of account you wish to create: (1) Create Savings Account   (2) Create Checking Account")
                                try:
                                    selection3 = int(input("Please enter option (1) or (2): "))
                                    if selection3 == 1:
                                        print("Lets create a savings account!\n")
                                        accNUM = int(input("Please enter your account number: "))
                                        attribute = formatAttributes(accNUM)
                                        if int(attribute[4]) >= 14:
                                            #attrib[3] = name, attrib[4] = age, attrib[1] = pin, attrib[0] = accNo, attrib[2] = balance
                                            bank_object_sav = SavingsAccount(str(attribute[3]), int(attribute[4]), int(attribute[1]), int(attribute[0]), int(attribute[2]))
                                            amount = int(input("Enter an initial amount to be placed into your savings: "))
                                            bank_object_sav.initialSavings(amount)
                                            bank_object_sav.viewBalance()
                                        else:
                                            print("Sorry, you must be aged 14 years or older to create this account")
                                    elif selection3 == 2:
                                        print("Creating Checking Account:\n")
                                        accNUM = int(input("Please enter you account number: "))
                                        attribute = formatAttributes(accNUM)
                                        if int(attribute[4]) >= 18:
                                            #attrib[3] = name, attrib[4] = age, attrib[1] =  pin, attrib[0] = accNo, attrib[2] = balance
                                            bank_object_checking = CheckingAccount(str(attribute[3]), int(attribute[4]), int(attribute[1]), int(attribute[0]), int(attribute[2]))
                                            amount = int(input("Enter an initial amount to be placed into your checking account: "))
                                            bank_object_checking.initialCheckingBal(amount)
                                            bank_object_checking.viewBalance()
                                        else:
                                            print("Sorry, you must be aged 18 years or older to create this account")
                                except ValueError:
                                    print("Please enter a valid option")
                            elif selection2 == 2:
                                # Read from account transactions file search for word in line then print line
                                print("A complete list of all transactions: ")
                                bank_object.printTransactions()
                            elif selection2 == 3:
                                print("Would you like to : (1) View Balance   (2) Deposit cash   (3) Transfer money   (4) Withdraw money ")
                                try:
                                    selection4 = int(input("Please select an option from above: "))
                                    if selection4 == 1:
                                        try:
                                            selection5 = int(input("Which account would you like to access the balance for?:  (1)General   (2)Savings   (3)Checking: "))
                                            if selection5 == 1:
                                                bank_object.viewBalance()
                                            elif selection5 == 2:
                                                try:
                                                    bank_object_sav = SavingsAccount()
                                                    accNo = int(input("Enter your Account number: "))
                                                    pin = int(input("Please enter in your bank pin: "))
                                                    bank_object_sav.login(accNo, pin)
                                                    bank_object_sav.viewBalance()
                                                except NameError:
                                                    print("There is no savings account associated with the account number you entered")
                                            elif selection5 == 3:
                                                try:
                                                    bank_object_checking = CheckingAccount()
                                                    accNo = int(input("Enter your Account number: "))
                                                    pin = int(input("Please enter you bank pin: "))
                                                    bank_object_checking.login(accNo, pin)
                                                    bank_object_checking.viewBalance()
                                                except NameError:
                                                    print("There is no checking account associated with the account number you entered")
                                        except ValueError:
                                            print("Please enter a valid option, (1), (2) or (3)")
                                    elif selection4 == 2:
                                        try:
                                            selection6 = int(input("Which account would you like deposit money to?:  (1)General   (2)Savings   (3)Checking:"))
                                            if selection6 == 1:
                                                amount = int(input("Enter the amount you wish to deposit to your general account: "))
                                                bank_object.depositFunds(amount)
                                            elif selection6 == 2:
                                                bank_object_sav = SavingsAccount()
                                                accNo = int(input("Enter your Account number: "))
                                                pin = int(input("Please enter you bank pin: "))
                                                bank_object_sav.login(accNo, pin)
                                                amount = int(input("Enter the amount you wish to deposit to your savings account: "))
                                                bank_object_sav.depositFunds(amount)
                                            elif selection6 == 3:
                                                bank_object_checking = CheckingAccount()
                                                accNo = int(input("Enter your Account number: "))
                                                pin = int(input("Please enter you bank pin: "))
                                                bank_object_checking.login(accNo, pin)
                                                amount = int(input("Enter the amount you wish to deposit to your checking account:"))
                                                bank_object_checking.depositFunds(amount)
                                        except ValueError:
                                            print("Please enter a valid option, (1), (2) or (3)")
                                    elif selection4 == 3:
                                        amount = int(input("Enter the amount you wish to transfer: "))
                                        accNo = int(input("Enter the account no. of the person you are sending the money to: "))
                                        bank_object.transferFunds(amount, accNo)
                                    elif selection4 == 4:
                                        try:
                                            selection7 = int(input("Which account would you like to withdraw from: (1)General  (2)Savings  (3)Checking:"))
                                            if selection7 == 1:
                                                amount = int(input("Enter the amount you wish to withdraw from your general account: "))
                                                bank_object.withdrawFunds(amount)
                                            elif selection7 == 2:
                                                bank_object_sav = SavingsAccount()
                                                accNo = int(input("Enter your Account number: "))
                                                pin = int(input("Please enter your bank pin: "))
                                                bank_object_sav.login(accNo, pin)
                                                if getattr(bank_object_sav, bank_object_sav.withdrew_date).days - date.today().days >= 30:
                                                    amount = int(input("Enter the amount you wish to withdraw from your savings account: "))
                                                    bank_object_sav.withdrawFunds(amount)
                                            elif selection7 == 3:
                                                bank_object_checking = CheckingAccount()
                                                accNo = int(input("Enter your Account number: "))
                                                pin = int(input("Please enter you bank pin: "))
                                                bank_object_checking.login(accNo, pin)
                                                amount = int(input("Enter amount you wish to withdraw from your checking account: "))
                                                bank_object_checking.withdrawFunds(amount)
                                        except ValueError:
                                            print("Enter valid option, (1)General, (2)Savings, (3)Checking")
                                except ValueError:
                                    print("Enter a valid option 1-4")
                            elif selection2 == 4:
                                try:
                                    selection8 = int(input("Which account would you like to delete: (1)Savings  (2)Checking:"))
                                    if selection8 == 1:
                                        print("Deleting your savings account")
                                        bank_object_sav = SavingsAccount()
                                        accNo = int(input("Enter your Account number: "))
                                        pin = int(input("Please enter you bank pin: "))
                                        bank_object_sav.login(accNo, pin)
                                        bank_object_sav.deleteAccount()
                                    elif selection8 == 2:
                                        print("Deleting your checking account")
                                        bank_object_checking = CheckingAccount()
                                        accNo = int(input("Enter your Account number: "))
                                        pin = int(input("Please enter you bank pin: "))
                                        bank_object_checking.login(accNo, pin)
                                        bank_object_checking.deleteAccount()
                                except ValueError:
                                    print("Enter valid option, (1)Savings (2)Checking")
                            elif selection2 == 5:
                                print("Now exiting Sara's banking services")
                                exit("Thank you, see you again soon!")
                    except ValueError:
                        print("Enter a valid option 1-5")
            elif option == 2:
                # registration
                name = input("Please enter in your fullname: ")
                age = int(input("Please enter your age: "))
                pin = int(input("Please create a 4 digit bank pin: "))
                accNo = random.randint(0, 99999)   # assigning the bank account a random (and hopefully unique) number
                cust = Customer(name, age)
                bank = BankAccount(name, age, pin, accNo)
                cust.addCustToFile()
                bank.writeBankToFile()

            elif option != 1 or 2:     #if they enter an option thats not available
                print("Please select a valid option")
    except ValueError:
        print('Please enter option (1), (2) or (3)')

main()  #call main function
