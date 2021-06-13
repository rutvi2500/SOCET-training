"""
HDFCBank->withdraw()
	->total max transaction  limit-3
	->total max amount limit-20,000
AXISBank->withdraw()
	->total max transaction limit-5
	->total max amount limit-30,000
(ATM Class)=>Main Class
1)user input choice for bank name
2)user input amount to withdraw
    ATM->inputAmount()=>Function
3)validate input amount limit->
   custom exception message(Max limit exceeded)
4)validate the max transaction limit->
    custom exception message(Max limit exceeded)
5)update the max amount limit and max transaction limit
 for successful transaction and print message also
6)Ask user for next transaction: yes/no
	if yes:
		contiue with sequence no (2)
	if no:
	    terminate the program
NOTE:
1)Terminate only when transaction max limit exceeded or
  amount max limit exceeded or
  user give no input for next transaction
2)mandatory to achieve encapsulation(__) and
  polymorphism(withdraw()) in program.
"""

global __maxt
global __max
__maxt=0
__max=0
class HDFC:
    def trans(self):
        __maxt=3
        return __maxt
    def amount(self):
        __max=20000
        return __max

class AXIS:
    def trans(self):
        __maxt=5
        return __maxt
    def amount(self):
        __max=30000
        return __max

class ATM:
    def validate(self,bankobject):
        tran=0
        lamount=int(bankobject.amount())
        print(f"Available balance: {lamount}")
        choice="y"
        while choice=="y":
            self.amount1=input("Enter the amount to withdraw: ")
            wamount=int(self.amount1)
            while int(tran)<int(bankobject.trans()):
                if wamount>0:
                    if int(self.amount1)<int(bankobject.amount()):
                        lamount-=wamount
                    else:
                        print("Exceeded transaction limit")
                        quit()
                tran+=1
                print(f"Remaining amount: {lamount} Withdrawal amount: {wamount}")
                if tran == int(bankobject.trans()):
                    print("Transaction Limit Exceeded")
                    quit()
                break
                print(tran)

            choice=input("Y/N").lower()

hdfc=HDFC()
axis=AXIS()
a=ATM()

in1=input("Enter 1 for HDFC and 2 for AXIS")
if in1=="1":
    a=ATM()
    a.validate(hdfc)
elif in1=="2":
    a=ATM()
    a.validate(axis)
else:
    quit()

