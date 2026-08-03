class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0): 
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts 
        
        
        #theri default value has bene set to 0 

    def __str__(self):
        return f"{self.galleons} Galleons {self.knuts} Knuts and {self.sickles} Sickles"


    def __add__(self, other):
        galleons = self.galleons + other.galleons
        knuts = self.knuts + other.knuts
        sickles = self.sickles + other.sickles 

        return Vault(galleons, knuts, sickles)
potter = Vault(100, 50, 20)
print(potter)

weasly = Vault(0, 0, 0)
print(weasly)


total = potter + weasly
print(total)# we have implemented an overloaded operator 

#we dannot define new operators in python as in arbitrary things cant be made into an operator 
