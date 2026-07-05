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