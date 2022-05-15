


class pubprivtest:
    def __init__(self):
        self._protectedVar = 'John' #defining a protectd variable, John. Protecting this variables helps ensure the data is more difficult to modify to maintain integrity of the class.
        self._protectedVar2 = 'Doe' #defining a protected var 2 just for testing purposes.
        self.__privateVar = 'Jane' #setting a private variable, which must be first retrieved from within the class and then set, making it even more difficult to modify, and ensures that any changes are intentional.
    def getPrivate(self): #Creating a method to retrieve our private variable from outside the class.
        print(self.__privateVar)
    def setPrivate(self, newPriv): #creating a method to allow setting the private variable from outside the class.
        self.__privateVar = newPriv #by assigning our privateVar to newPriv, we can ensure that if one intends to adjust the value of __privateVar, they must specifically call the function setPrivate and use the newPriv parameter to change.

obj = pubprivtest()
obj._protectedVar = 'Jonathan'
# _protectedVar2 = Jimmy #Notice that if it is not called from within the class, _protectedVar2 is not defined.
print(obj._protectedVar + ' ' + obj._protectedVar2)

obj.getPrivate() #printing the private variable before we set it.
obj.setPrivate('Mary') #setting the private variable by calling the setPrivate function.
obj.getPrivate() #printing the private variable once we have redefined it to Mary.

