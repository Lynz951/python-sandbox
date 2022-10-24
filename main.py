# age = 20
# price = 19.95
# first_name = "Lindsay"
# is_online = True
# print(age)

# name = input("What is your name? ")
# print("Hello " + name)

# birth_year = input("Enter your birth year: ")
# age = 2022 - int(birth_year)
# print(age)

# First: 10
# Second: 20

# first = input("First: ")
# second = input("Second")
# sum = int(first) + int(second)
# print("Sum: " + str(sum))

# course = 'Python for Beginners'
# print(course.find('y')) #1
# print('Python' in course) #True

# x=10
# x += 3 
# print(x)

# price = 25
# print(price > 10 and price < 30)

# temperature = 5

# if temperature > 30:
#     print("It's a hot day!")
#     print("Drink plenty of water")
# elif temperature > 20:
#     print("It's a nice day!")
# elif temperature > 10:
#     print("It's a bit cold!")
# else:
#     print("Its freezing")
# print("Done")

# Weight: 170

# weight = int(input("Weight: "))
# unit = input("(K)g or (L)bs: ")
# if unit.upper == "K":
#     converted = weight/0.45
#     print("Weight in Lbs: " + str(converted))1
# else:
#     converted = weight * 0.45
#     print("Weight in Kgs: " + str(converted))

# i = 1
# while i <= 5:
#     print(i * "*")
#     i = i + 1

# names = ["Lindsay", "Amy", "Molly"]
# print(names[0:2])

# numbers = [1, 2, 3, 4, 5]
# for item in numbers:
#     print(item)

# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i = i + 1

# class Car:
#     def __init__(self, input_model):
#         self.model = input_model
#         self.mileage = 0

#     def vroooooom(self, distance):
#         self.mileage += distance

#     def __str__(self):
#         return f"Hello, I am a {self.model} and I have travelled {self.mileage} miles"

# my_car = Car('Honda')
# print(my_car.model)
# print(my_car.mileage)
# my_car.vroooooom(1234)
# print(my_car.mileage)
# print(my_car)

#initial sub-sequence of the Fionacci series
# a, b = 0, 1
# while a < 1000:
#     print(a, end=',')
#     a, b = b, a+b

# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))

users = {'Lindsay': 'active', 'Amy': 'inactive', 'Molly': 'active'}
for user, status in users.copy().items():
    print(users)
    if status == 'inactive':
        del users[user]   
        print(users)
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
        print(users)
        