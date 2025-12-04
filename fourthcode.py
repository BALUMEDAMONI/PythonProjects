x = 5
y = 15
print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)
a = [1, 2, 3, 4, 5]
b = []
for i in a:
    b.append(i * i)
print("Squares:", b)
name = "Balu"
course = "Computer Science"
print("Name:", name)
print("Course:", course)
total = 0
for n in range(1, 21):
    total += n
print("Sum 1-20:", total)
even_nums = [n for n in range(30) if n % 2 == 0]
print("Even numbers:", even_nums)
def multiply(a, b):
    return a * b
print("Multiply 7 and 8:", multiply(7, 8))
def greet(user):
    return "Hello, " + user
print(greet("Balu"))
fruits = ["apple", "banana", "mango", "orange"]
for fruit in fruits:
    print("Fruit:", fruit)
person = {"name": "Balu", "age": 20, "city": "Sheffield"}
print("Person:", person)
for key in person:
    print(key, ":", person[key])
numbers = [10, 20, 30, 40]
for value in numbers:
    print("Number:", value)
