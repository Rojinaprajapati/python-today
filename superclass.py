class Parent:
    def __init__(self,lastname,height,age,looks):
        self.lastname=lastname
        self.height=height
        self.age=age
        self.looks=looks

    def getLastname(self):
        return self.lastname
    
    def getheight(self):
        return self.height
    
    def getAge(self):
        return self.age
    
    def getlooks(self):
        return self.looks
        
class Child(Parent):
    def __init__(self, lastname, height, age, looks,weight,firstname):
        super().__init__(lastname,height,age,looks)
        self.weight=weight
        self.firstname=firstname

    def getfirstname(self):
        return self.firstname
    def getWeight(self):
        return self.weight
tekendra=Child("Rai","5",21,"Hot",30," Tekendra")
# print("Last Name : ",tekendra.getLastname())
# print("Height : ",tekendra.getheight())
# print("Age : ",tekendra.getAge())
tekendra.looks="Ugly"
# print("Looks : ",tekendra.looks)
# print("Weight : ",tekendra.getWeight())

print("Hello My name is {0} {1}. I am {2} years old. I am {3} ft in height.I am very {4}. I am {5} kg. My father name is Prabhat Rai ..".format(tekendra.getfirstname(),tekendra.getLastname(),tekendra.getAge(),tekendra.getheig        