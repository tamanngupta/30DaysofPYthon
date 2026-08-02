class Student(): 
    def __init__(self, name, house): #the first parameter is just the memory storage so always remember that the first attribute is storage SELF IS TO STORE IN THE OBJECT THAT YOU JUST CREATED  
        if not name:
            raise ValueError
        
        #__str__ is used to call function when anyone wants to see your function as a string 
        if house not in ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff']:
            raise ValueError('Invalid house name')
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student) #we are calling student as a string so we need to add the __str__method 

def get_student():
    name = input('Name: ')
    house = input('House: ')
    student = Student(name, house) #this line is a constructor it constructs student. due to the self parameter that we used we dont have to 
    return student

if __name__ == '__main__':
    main()

    # we can use sys.ecit to exit the program 
    #in dictionary if you enter an attribute it has to accept it however in class you have complete control over the data you want to accept 
#we can also import classes in other files 
#if I do house = None so I can either assign a value to house otherwise it is optional
#we can create our own errors with classes as well
