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

# users = {'Lindsay': 'active', 'Amy': 'inactive', 'Molly': 'active'}
# for user, status in users.copy().items():
#     print(users)
#     if status == 'inactive':
#         del users[user]   
#         print(users)
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status
#         print(active_users)

# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()
        
# >>> def fib(n):
# ...     a, b =0, 1
# ...     while a < n:
# ...             print(a, end=' ')
# ...             a, b = b, a+b
# ...     print()
# ... 
# >>> fib(2000)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 
# >>> def fib2(n):
# ...     result = []
# ...     a, b = 0, 1
# ...     while a < n:
# ...             result.append(a)
# ...             a, b = b, a+b
# ...     return result
# ... 
# >>> f100 = fib2(100)
# >>> f100
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]     

# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)
#         ask_ok('Do you really want to quit?')
        
stopped at 4.8.2 Keyword arguments