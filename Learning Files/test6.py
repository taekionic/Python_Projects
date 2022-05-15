

def getInfo():
    var1 = input("\nPlease provide the first numeric value: ")
    var2 = input("\nPlease provide the second numeric value: ")
    return var1,var2


def compute():
    go = True
    while go:
        var1,var2 = getInfo()
        try:
            var3 = int(var1) + int(var2) #converts the input, which is returned as a string, back into an integer
            go = False
        except ValueError as e: #allows you to provide the specific computing error to the user
            print("{}: \n\nYou did not provide a numeric value!".format(e))
        except: 
            print("\n\nOops, you provided invalid inpuit. Program will close now!")
        """finally:
            print("Moving on...")"""
    print("{} + {} = {}".format(var1,var2,var3))







if __name__ == "__main__":
    compute()