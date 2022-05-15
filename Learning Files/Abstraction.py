from abc import ABC, abstractmethod

class bankbalance(ABC):
    def __init__(self):
        self.__privateBalance = 1000
    def getBalance(self):
        return self.__privateBalance

    def funds(self, withdrawal):
        print("Your withdrawl request was: ", withdrawal)

    @abstractmethod
    def withdrawalrequest(self, withdrawal):
        pass


class Request(bankbalance):
    def withdrawalrequest(self, withdrawal):
        self.bal = self.getBalance()
        self.difference = (withdrawal - self.bal)
        print(f'You do not have enough funds to make this withdrawl.\n Your balance is ${self.getBalance()}. \n Your withdrawal request was ${withdrawal}. \n To make this withdrawal, please deposit ${self.difference}')


obj = Request()
obj.funds(4000)
obj.withdrawalrequest(4000)