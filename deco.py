def greet():
    print('hello')

def run(func):
    func()

run(greet)

def outer():
    def inner():
        print('in')
    return inner

x = outer()
x()

def decorator(func):

    def wrapper():
        print('before')
        func()
        print('after')
    return wrapper

@decorator
def gg():
    print('hello')


gg()


def upp(function):
    def wrap(): 
        func = function()
        make_upper = func.upper()
        return make_upper
    return wrap

def spi(function): 
    def wap(): 
        func =function()
        splt = func.split()
        return splt
    return wap

@spi
@upp

def funct():
    return 'welcome to python'

print(funct())

def decorator_with_parameters(function):
    def accept_wrap(para1, para2, para3):
        # 1. Capture the return value of the original function
        result = function(para1, para2, para3)
        
        # 2. Do the decorator's side-effect (printing)
        print('I live in {}'.format(para3))
        
        # 3. Explicitly return the original function's result
        return result
    return accept_wrap

@decorator_with_parameters
def funn(first_name, last_name, country):
    print('My name is {} {}'.format(first_name, last_name))

funn('tamanna', 'Gupta', 'India')

ames = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

def make_upper(name):
    return name.upper()

change_upper_names = map(make_upper, ames)
print(list(change_upper_names))


numbers = [45,65,34,76,32]

def is_even(num):
    if num % 2 == 0 :
        return True
    else : 
        return False
    
lets_check = filter(is_even, numbers)
print(list(lets_check))