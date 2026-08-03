class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError('Missing name')


class Student(Wizard): #this means when I define a student class go ahead and inherit all the attributes of the superclass
    def __init__(self, name, house):
        super().__init__(name)
    

        self.house = house 


class Professor(Wizard):
    def __init__(self, subject):
        super().__init__(name). #this is the way of accesing the parent class and calling the initialising method 
        self.subject = subject



student = Student('Harry', "gryffindor")
professor = Professor('Minerva', 'transfiguration ')
wizard = Wizard('Albus')

#ok so the problem is that I need the if not name error for both of them. so when you see classes that have somewhat similar code but in all honestly do not need to exist parallely we use inheritance 
#inheretamce is that one class should inherit from other 
#exceptions are actually forms of inheritance there are all hierachal in nature 



#operator overloading is changging what a an opertor can be used for you can add functions to a particular function 

