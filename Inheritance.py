class Parent:
     def __init__(self , name, age):
          self.firstname = name
          self.age = age
     def view(self):
         print(self.firstname , self.age)
class Child(Parent):
     def __init__(self , name , age):
          Parent.__init__(self, name, age)
          self.lastname = "Teknik Informatika"
     def view(self):
          print("Pemrograman Visual" , self.firstname ,  self.age , self.lastname)
ob = Child("Muh.Rifki Anhar" , '2019')
ob.view()
