# Q1. What is Abstraction in OOps? Explain with an example.
# Answer-
'''Abstract class can be considered a skelton or blueprint for other classes.It is used to hide complex implementation details and expose only
the essential features of an object or system.'''
# example
import abc

class shape:
    
    @abc.abstractmethod
    def area(self):
        pass
    
class rectangle(shape):
    
    def __init__(self, width , height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
class circle(shape):
    
    def __init__(self , radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius * self.radius
    
rect = rectangle(8,4)
print(rect.area())

circle = circle(8)
print(circle.area())

# Q2. Differentiate between Abstraction and Encapsulation. Explain with an example.
# Answer-
'''Abstraction-
Definition: Abstraction is about hiding the complexity and showing only the necessary details of an object or system.
            It focuses on what an object does, rather than how it does it.
Example: When you use a TV remote, you only interact with buttons like "Power On" or "Volume Up,"
         without knowing the complex electronics inside the remote or TV.
Encapsulation-
Definition: Encapsulation is about bundling data (variables) and methods that operate on that data into a single unit or class. 
            It also restricts direct access to some of the object’s components, which is known as data hiding.
Example: When you use a capsule for medicine, it hides the ingredients inside the capsule, and you cannot see or modify what's inside. 
         You just use the capsule as it is.'''

# here's a combined example of Abstraction and Encapsulation 
import abc

# Abstract class (Abstraction)
class ATM:
    
    @abc.abstractmethod
    def deposit(self , amount):
        pass
    
    @abc.abstractmethod
    def withdraw (self , amount):
        pass
    
    @abc.abstractmethod
    def get_balance(self):
        pass
    
class bank(ATM):
    
    def __init__(self , balance = 0):
        self.__balance = balance        # Private variable (Encapsulation)
        
    def deposit(self , amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited amount:",amount, "New balance:", self.__balance)
        else:
            print("deposited amount must be positive")
            
    def withdraw(self , amount):
        if amount > 0 :
            self.__balance -= amount 
            print("Withdraw:",amount,"New balance:", self.__balance)
        else:
            print("Insufficient funds or invalid amount.")
            
    def get_balance(self):
        return self.__balance

bank_account = bank()

bank_account.deposit(1000)
bank_account.withdraw(300)
print("Total balance:",bank_account.get_balance())

# Q3. What is abc module in python? Why is it used?
# Answer-
'''abc module-The abc module in Python stands for Abstract Base Classes. It provides the infrastructure for defining abstract classes.
Used:
    The primary use of the abc module is to define abstract base classes and enforce certain methods to be implemented by any subclass
    that inherits from the abstract class. '''
    
# Q4. How can we achieve data abstraction?
# Answer-
'''Data abstraction can be achieved through various techniques that focus on hiding the implementation details and exposing only the 
essential parts that are needed for interaction. 
Ways to Achieve Data Abstraction:
    1. Abstract Classes and Methods
    2. Encapsulation (Using Private Members)
    3. Properties (Using @property in Python)
    4. Interfaces or APIs(that abstract away the underlying complexity)'''

# Q5. Can we create an instance of an abstract class? Explain your answer.
# Answer-
'''No, we cannot create an instance of an abstract class.

 An abstract class is designed to be a blueprint for other classes. It may contain abstract methods (methods that are declared but contain
 no implementation) that must be implemented by any non-abstract subclass.

If you try to instantiate an abstract class directly, Python will raise a TypeError.'''
# Example 

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

# Trying to instantiate an abstract class
animal = Animal()  # This will raise a TypeError

'''Since Animal is an abstract class and its sound method has no implementation, the class is incomplete. To create an object, a concrete
subclass must implement the sound method, at which point an instance of the subclass can be created.'''  