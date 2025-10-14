import time
# age = int(input("How old are you?: "))
#
# if age >= 18:
#     print("You are an adult.")
# elif age < 0:
#     print("You haven't been born yet")
# else:
#     print("You are a child")

## and, or, not

# temp = int(input("What is the temperature outside? "))
#
# if not(temp >= 0 and temp <= 30):
#     print("the temperature is bad today!")
#     print("go inside")
# elif not(temp < 0 or temp > 30):
#     print("the temperature is good today!")
#     print("go outside")

## while loop
# name = ""
#
# while not name:
#     name = input("Enter your name: ")
#
# print("Hello " + name)

## for loop
# for i in range(10):
#     print(i)
# for i in range(50, 100 + 1,2):
#     print(i)

# for i in "hello":
#     print(i)

# for second in range(10,0,-1):
#     print(second)
#     time.sleep(1)
# print("happy new year!!")

## nested loop

# row = int(input("Enter row: "))
# col = int(input("Enter column: "))
# symbol = input("Enter symbol: ")
#
# for i in range(row):
#     for j in range(col):
#         print(symbol, end="")
#     print()

## Loop control statement - break, continue, pass
# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break

# phone_number = "112-345-6789"
#
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")

for i in range(20):
    if i == 13:
        pass
    print(i)