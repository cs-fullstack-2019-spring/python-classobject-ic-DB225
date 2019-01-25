def main():
    #problem1()
    #problem2()
    problem3()
    #problem4()
    #challenge()

#PROBLEM1
#Create a Dinner class with attributes dishName, protein, veggie, and price.
# In the class, create a function that will print all attributes.
# Create an object of Dinner in your problem1 function and print all of it's attributes.
def problem1():
    class Dinner:
        def __init__(self,dishName, protein, veggie, price):
            self.dishName = dishName
            self.protein = protein
            self.veggie = veggie
            self.price = price

        def __str__(self):
            return(f"{self.dishName}, {self.protein}, {self.veggie}, {self.price}")
    newDinner = Dinner("Fried rice","Rice","tomato",100)
    print(newDinner)


##################################################################################
#PROBLEM2
#Create a function that has a loop that quits with ‘0’.
# If the user doesn't enter '0', ask them to input another string.
def problem2():
    userInput = ''
    while(userInput != '0'):
        userInput = input("Put a string : ")

##################################################################################
#PROBLEM3
#Create an Account class with attributes: name, balance, and creationDate.
#The class should have an updateBalance function that can update the balance
# and a printNameAndBalance function that will print the name and balance of an object.
#a) Create an account named "Kenn" with $50
#b) Create an account named "Kevin" with $95
#c) Print the Kenn account and the Kevin acccount
#c) Add $15 to the Kenn account through the function
#d) Remove $10 from the Kevin account
#e) Print the Kenn account and the Kevin acccount
def problem3():
    class Account:
        def __init__(self,name, balance, creationDate):
            self.name = name
            self.balance = balance
            self.creationDate = creationDate

        def updateBalance(self,newBalance):
            self.balance += newBalance

        def __str__(self):
            return(f"The account of {self.name} is ${self.balance}, created in {self.creationDate}")

    newAccount1 = Account("kenn",50,2019)
    newAccount2 = Account("Kevin",95,2019)


    print(newAccount1)
    print(newAccount2)
    newAccount1.updateBalance(15)
    newAccount2.updateBalance(-10)
    print(newAccount1)
    print(newAccount2)


##################################################################################
#PROBLEM4
#Create a ToDo class.
# Create the attributes: name, dueDate, list (this should be an array).
# Create a function that can add a string to the list.
# Create an object of ToDo in your problem4 function and print all of it's attributes.
#def problem4():
class ToDo:
    def __init__(self, name="", dueDate="1963/01/01", list=[]):
        self.name = name
        self.dueDate = dueDate
        self.list = list

    def addStringToList(self, newItem):
        self.list.append(newItem)

    def printOutToDoList(self):
        for x in self.list:
            print(x)

    def printAll(self):
        print(self.name, self.dueDate, self.list)

    def removeToDoItem(self):
        userInput = input("What do you want to remove?")
        self.list.remove(userInput)

    kennToDoList = ToDo("Kenn's List", "2019/01/25", ["blah", "blahblah","grade classwork", "make questions harder"])
    kennToDoList.printAll()
    kennToDoList.removeToDoItem()
    kennToDoList.printAll()




























##################################################################################
if __name__ == '__main__':
    main()