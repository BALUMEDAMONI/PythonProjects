x = 10
y = 3
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
numbers = [1, 2, 3, 4, 5]
doubled = []
for n in numbers:
    doubled.append(n * 2)
print("Doubled:", doubled)
name = "Balu"
city = "Sheffield"
print("Name:", name)
print("City:", city)
total = 0
for i in range(1, 11):
    total += i
print("Sum 1 to 10:", total)
even_numbers = [n for n in range(20) if n % 2 == 0]
print("Even numbers:", even_numbers)
def square(num):
    return num * num
print("Square of 6:", square(6))
fruits = ["apple", "banana", "orange"]
for f in fruits:
    print("Fruit:", f)
person = {"name": "Balu", "age": 20, "country": "UK"}
print(person)
