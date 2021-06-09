"""
user will input data for SignUp class-Constructor
    fn,ln,un,pwd
    pwd must fulfil below given criteria
        minmum 8 characters
        maximum 16 characters
        at least one lowercase
        at least one uppercase
        at least one digit
        at least one special character
    if not matched then print custom message with exception
    and give chance again till condition not satisfied
user will input data for SignIn class-Constructor
    un,pwd
    compare SignUp (un and pwd) with (SignIn un and pwd)
        loginCheck()-Function
        if not matched then print custom message with exception
        else print welcome message with fn and ln
"""
import re

# Parent Class
class SignUp:
    def __init__(self, fn, ln, un):
        self.fn = fn
        self.ln = ln
        self.un = un

    def validate(self):
        # This function check for password charecterstics such as len,upper,lower,symbol and digit.
        while True:
            self.password = input("Enter a password: ")
            try:
                if len(self.password) <= 8 or len(self.password) >= 16:
                    raise ValueError("Make sure your password is at least 8 letters and at max 16 letters")
            except ValueError as ve:
                print(ve)

            try:
                if re.search('[0-9]', self.password) is None:
                    raise ValueError("Make sure your password has a number in it")
            except ValueError as ve:
                print(ve)

            try:
                if re.search('[A-Z]', self.password) is None:
                    raise ValueError("Make sure your password has a capital letter in it.")
            except ValueError as ve:
                print(ve)

            try:
                if re.search('[a-z]', self.password) is None:
                    raise ValueError("Make sure your password has a lowercase letter in it.")
            except ValueError as ve:
                print(ve)

            try:
                if re.search('[+]', self.password) is None:
                    raise ValueError("Make sure your password has a symbol in it.")
            except ValueError as ve:
                print(ve)

            else:
                print("Your password seems fine")
                global password
                password = self.password
                break
            # This class is used to sign in


class SignIn(SignUp):
    def __init__(self, inun):
        SignUp.__init__(self, fn, ln, un)
        self.inun = inun
        self.inpwd = inpwd

    def loginCheck(self):
        if self.inun == self.un and self.inpwd == password:
            print(f"Welcome {self.fn} {self.ln}")
        else:
            raise ValueError("Your password didn't match.")


print("===================Sign Up Process=================")
fn = input("Enter First Name: ")
ln = input("Enter Last Name: ")
un = input("Enter User Name: ")
c = SignUp(fn, ln, un)
c.validate()

print("================Sign In Process===================")
inun = input("Enter Your User Name: ")
inpwd = input("Enter Your Password: ")

b = SignIn(inun)
b.loginCheck()