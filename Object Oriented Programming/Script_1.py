# Need of OOP

# Assuming we are storing the data about a software engineer,
# It has multiple fields such as name , salary ect.
# If we choose list , it will be as follows

se1 = ["SoftwareEngineer","Sushanth",20,"junior",5000]      
se2 = ["SoftwareEngineer","ujwal",20,"senior",7000] 

# Clearly we can see that this is not the best data structure possible 
# It is error prone

# To overcome this problem classes are used, classes are used.
# More complex data sctructes canbe obtained using classes.
# They also include functions within them , which enables to use function
# directly on object(Instance of the class).

# A Class is a """blue print""" of how our data structure should look like

# Syntax : camel casing

class SoftwareEngineer:

    # Class attribute
    alias = "Keyboard Magician" 
    # Class attribute is accesiible 

    def __init__(self,name,age,level,salary):   #It is a special method to initialise out object
                                                # name ,age ,level,salary are parameters are passed from outside
        # instance attributes
        self.name = name
        self.age = age
        self.level  = level                     # self.attribute = parameter
        self.salary = salary
        # instance attribute only belongs to the object not the entire class





# Instantace of the class

se1 = SoftwareEngineer("Sushanth",20,"junior",5000)


print(type(se1))
print(se1.name)
print(se1.age)

# print(SoftwareEngineer.name) Results error because name is an instance attribute
print(SoftwareEngineer.alias)  # is a class attribute and valid
print(se1.alias)               # class attribute can be used in an instance


se2 = SoftwareEngineer("ujwal",20,"senior",7000)
print(SoftwareEngineer.alias)  # is a class attribute and valid
print(se2.alias)               # class attribute can be used in an instance


# all of the above properties applies