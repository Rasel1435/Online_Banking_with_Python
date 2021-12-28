# Task 8
# online Banking
# Account Create, Close, Pin Change
# Transaction Deposit, Withdrow, Transfer


database = {}
initial_acc = 10000

import re


class Account:
    bank = 'Some Bank'

    def __init__(self, name: str, age: int, gender: str, ph: str, email: str):
        self.name       = name
        self.age        = age
        self.gender     = gender
        self.ph         = ph
        self.email      = email
        self.balance    = 0.0
        self.is_active  = True
        self.pin        = name.strip()[:4]+ph[-4:]

    def validate(self):
        namevalid   = True if re.match(r'^[a-zA-Z\s]{5,30}$', self.name) else False
        agevalid    = True if self.age > 12 and self.age < 60 else False
        gendervalid = True if self.gender.lower() in ['male', 'female'] else False
        phvalid     = True if re.match(r'^\+88[0-9]{11,11}$', self.ph) else False
        emailvalid  = True if re.match(r'^[a-z]+[a-z0-9_]\w*@gmail.com$', self.email) else False
        return all([namevalid, agevalid, gendervalid, phvalid, emailvalid])
        

    def create(self):
        global database
        if self.validate():
            global initial_acc 
            initial_acc += 1
            database[initial_acc] = self
            return initial_acc
        else:
            return "Validation Unsuccessfull!"

    
    def close(self, pin:str):
        if self.is_active:
            if pin == self.pin:
                self.is_active = False
                return 'Closed!' 
            else:
                return "Invalid Pin!"
        else:
            return "Already Closed!"


    def deposit(self, amount:float):
        if self.is_active:
            self.balance += amount
            return self.balance
        else:
            return 'Account Not Active!'


    def withdraw(self, amount:float, pin:str):
        if self.is_active:
            if self.balance> amount and pin == self.pin:
                self.balance -= amount
                return self.balance
            else:
                return "Insufficient Blance or Invalid PIN"
        else:
            return 'Account is Not Active!'

    
    def transfer(self, amount:float, pin:str, to_ac:int):
        global database
        if self.is_active and database.get(to_ac):
            if self.balance> amount and pin == self.pin:
                other = database[to_ac]
                self.balance -= amount
                other.balance += amount
                return self.balance
            else:
                return "Insufficient Blance or Invalid PIN"
        else:
            return 'Account is Not Active! or Account not Found!'
        


rasel = Account('Rasel Shiekh',24, 'Male', '+8801644425997', 'rasel@gmail.com')
rasel.validate(), rasel.create()


rasel = database[10001]
rasel.is_active

nirob = Account('Nirob Ahmed',24, 'Male', '+8801644425999', 'nirob@gmail.com')
nirob.validate(), nirob.create()

nirob = database[10002]
nirob.is_active

rasel.balance, nirob.balance

rasel.deposit(10000)

rasel.transfer(5000, 'Rase5997', 10002)

database[10001].balance, database[10002].balance

