class MyClass():

 # Constructor, called whenever an instance of the class is created.
 def __init__(self, my_greeting):
    print("Running constructor for JORzClass")
    # Create attributes and set initial values
    self.message = my_greeting
 def my_method(self):
    print(self.message)
    #Object created to call class
my_class1 = MyClass("Morning everyone!")
my_class2 = MyClass("Lets get ready!")
my_class1.my_method()
my_class2.my_method()
print(type(my_class1))
print(type(my_class2))