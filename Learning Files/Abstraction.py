from abc import ABC, abstractmethod

class bankbalance(ABC):
    def __init__(self): #defining a private variable that contains the bank balance of an account. 
        self.__privateBalance = 1000
    def getBalance(self): #defining a method to retrieve the private balance. 
        return self.__privateBalance

    def funds(self, withdrawal): #defining a method to print the withdrawal request amount. This value will be passed to the abstract method below.
        print("Your withdrawal request was: ", withdrawal)

    @abstractmethod #this function is instructing us to pass an argument, but without any information on how or what kind of data.
    def withdrawalrequest(self, withdrawal):
        pass


class Request(bankbalance):
    def withdrawalrequest(self, withdrawal): #here, we are defining how to implement the withdrawal request function from above, as well as retrieving our private balance and comparing the two values to return the difference. 
        self.bal = self.getBalance()
        self.difference = (withdrawal - self.bal)
        print(f'You do not have enough funds to make this withdrawl.\n Your balance is ${self.getBalance()}. \n Your withdrawal request was ${withdrawal}. \n To make this withdrawal, please deposit ${self.difference}')


obj = Request()
obj.funds(4000)
obj.withdrawalrequest(4000)