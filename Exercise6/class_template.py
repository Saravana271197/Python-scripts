#Class MyClass template
class MyClass:
# __init__ function initiated when class is called
  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
# class method used inside class
  def info(self):
    print("Hello my name is " + self.name)
# object v used to call the class and method
v = MyClass("Saravana", "Pandian")
v.info()