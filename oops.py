class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
      #so this line and main will go through our setters 

    def __str__(self):
        return f"{self.name} from {self._house}"

    @property
    def house(self):
        return self._house

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError
        self._name = name
    @house.setter
    def house(self, house):
        if house.lower() not in ['slytherin', 'gryffindor', 'hufflepuff', 'ravenclaw']:
            raise ValueError('Invalid house name')
        self._house = house

def main():
    student = get_student()
    print(student)
    
def get_student():
    name = input('name: ')
    house = input('house')
    student = Student(name, house)
    return student 

if __name__ == '__main__':
    main()
