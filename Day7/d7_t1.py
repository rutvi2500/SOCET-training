"""
BankInfo-Class
    first name
    last name
    gender
    address
BankAccount-Class
    acno
    amount
    object_BankInfo
Saving-Class
    minAmount = 10000
    rate=6%
Current-Class
    minAmount = 5000
    rate=None
Main-Class
    user will input data for BankInfo-Constructor
    user will input data for BankAccount-Constructor
        acno=>generate 13 digit random int number=>random library
    input Amount
    user will select Saving or Current
    validate the amount given by user-Function
        give 3 chances
        after 3 chances-program exit
    input months
    calculate the interest-Function (Saving)
    message for Current Class=>Interest is unavailable for current account
    Display the whole profile-Function
"""

import random

class BankInfo:
    def __init__(self, firstname, lastname, gender, address):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.address = address

class BankAccount:
    def __init__(self, bankInfo, acno, amount):
        print("in BankInfo")
        self.acno = acno
        self.amount = amount
        self.bankInfo = bankInfo

class Saving(BankAccount):
    minAmount = 10000
    rate = 6
    interest = 0.0
    def validate(self):
        if self.amount >= self.minAmount:
            pass
        else:
            for i in range(4):
                if self.amount >= self.minAmount:
                    pass
                elif i == 3:
                    print("Your 3 Chances Is Finish!")
                    exit()
                else:
                    self.amount = int(input("Enter Amount 10000 or Above:"))
    def interestCalculate(self, months):
        self.months = months
        year = self.months / 12
        self.interest = float((self.amount * self.rate * year) / 100)
    def viewProfie(self):
        print("Complete Profile For Your Saving Account")
        print("FirstName=", self.bankInfo.firstname,
              "\nLastName=", self.bankInfo.lastname,
              "\nGender=", self.bankInfo.gender,
              "\nAddress=", self.bankInfo.address,
              "\nAccount Number=", self.acno,
              "\nAmount=", self.amount,
              "\nRate=", self.rate,
              "\nMonths=", self.months,
              "\nInterest=", self.interest)


class Current(BankAccount):
    minAmount = 5000
    rate = None
    def validate(self):
        if self.amount >= self.minAmount:
            pass
        else:
            for i in range(4):
                if self.amount >= self.minAmount:
                    break
                elif i == 3:
                    print("Your 3 Chance Is Finish!")
                    exit()
                else:
                    self.amount = int(input("Enter Amount 5000 or Above:"))
    def viewProfie(self):
        print("Complete Profile For Your Current Account")
        print("FirstName=", self.bankInfo.firstname,
              "\nLastName=", self.bankInfo.lastname,
              "\nGender=", self.bankInfo.gender,
              "\nAddress=", self.bankInfo.address,
              "\nAccount Number=", self.acno,
              "\nAmount=", self.amount,
              "\nRate=", self.rate,
              "\nNo Interest Available For Current Account !")


class Main:
    def __init__(self):
        f = input("Enter Your First Name:")
        l = input("Enter Your Last Name:")
        g = input("Enter Your Gender:")
        a = input("Enter Your Address:")
        bankInfo = BankInfo(f, l, g, a)
        ac = random.randint(0000000000000, 9999999999999)
        am = int(input("Enter Your Amount:"))
        print("Select Your Account Type:-1.Saving 2.Current")
        n = int(input("Enter No. 1 or 2:-"))

        if n == 1:
            saving = Saving(bankInfo, ac, am)
            saving.validate()
            months = int(input("Enter Your Months:"))
            saving.interestCalculate(months)
            saving.viewProfie()

        elif n == 2:
            current = Current(bankInfo, ac, am)
            current.validate()
            months = int(input("Enter Your Month:"))
            current.viewProfie()
objectMain = Main()


"""
from random import *

class BankInfo:
    def __init__(self, fn, ln, gen, add):
        self.fn = fn
        self.ln = ln
        self.gen=gen
        self.add=add

# Child Class
class BankAccount(BankInfo):
    def __init__(self,acc_no,amount):
        self.acc_no = acc_no
        self.amount = amount

class Saving(BankAccount):
    def __init__(self,amount):
        super().__init__(self,amount)
        month=int(input("Enter Month"))
        new_amount=self.amount*0.06*month/12
        interest=self.amount + self.new_amount
        print(new_amount)
        print(interest)

    def __repr__(self):
        return f"interest is {self.interest}"

ls=[]

class main(Saving,BankAccount,BankInfo):
    def __init__(self):
        fn = input("Enter First Name: ")
        ln = input("Enter Last Name: ")
        gen = input("Enter Gender: ")
        add = input("Enter your address: ")
        acc_no= randint(1000000000000, 9999999999999)
        print("Account number is ",acc_no)
        amount = int(input("Enter your amount: "))
        act=input("Enter S for saving account and C for current account: ")
        if(act=="S" or act=="s"):
            b=Saving()
        elif(act=="C" or act=="c"):
            print("No interest for Current account.")

        S = BankInfo(fn, ln, gen, add)
        print(S)

main()

"""
