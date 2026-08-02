class Student:
    #when a function is inside a class its known as method. init and str are special methods that python has built in 
    def __init__(self, name, house):
        self.name = name
        self.house = house 
        if not name:
            raise ValueError
        if house not in ['Gryffindor', 'slytherin', 'Hufflepuff', 'RavenClaw']:
            raise ValueError('Invalid house name')
    
    def __str__(self):
        return f"{self.name} from {self.house}."


#getter
    def house(self):
        return self.house
#setter
    def house(self, house):
        if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'slytherin']
        self.house = house 
#a getter is a function for the class that gets some attribute. a setter sets some value. 

#whenever you create a function in a class it always must take one attribute which is self to give you access to the current object in question
   
#we can circumvent conditions that are built in the classes by harcoding them later on
#therefore even thought we have more control over the code we can still modifyl things 
#a property is just an attribute that has more defence mechanisms in plac. It is a function in python. IT IS A DECORATOR.

def main():
    student = get_student()
    print(student)

def get_student():
    name = input('name: ')
    house = input('house: ')
    student = Student(name, house)
    return student




if __name__ == '__main__':
    main()
