#Day 2: 30 Days of Python programming

first_name = 'Tamanna'
last_name = 'Gupta'
full_name ="Tamanna Gupta"
Country = "India"
city = "Delhi"
age = 18
year = 2026
is_married = False
is_true = "works hard"
is_light_on = True
how_do_I_feel, What_is_the_day, What_is_the_temmperature = 'elated', 'tuesday', "50 degree celsius"

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(Country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(how_do_I_feel))
print(type(What_is_the_day))
print(type(What_is_the_temmperature))

len(first_name)
len(last_name)
print(min(len(first_name), len(last_name)))

num_one = 5
num_two = 4
total = num_one + num_two
print(total)
diff = num_one - num_two
print(diff)
product = num_one * num_two
print(product)
division = num_one / num_two
print(division)
remainder = num_one % num_two
print(remainder)
power = num_one ** num_two
print(power)

floor_division = num_one // num_two
print(floor_division)

radius = 30
area_of_a_circle = 3.14*radius**2
print(area_of_a_circle)
circum_of_circle = 2*3.14*radius
print(circum_of_circle)

input_radius = input("Enter the radius of a circle: ")
area_of_circle = 3.14*float(input_radius)**2
print(area_of_circle)

input_frst_name = input("Enter your first name: ")
input_last_name = input("Enter your last name: ")
full_name = input_frst_name + " " + input_last_name
print(full_name)