# food = ["pizza", "hamburger", "burger", "spaghetti"]
# food[0] = "sushi"
# food.append("ice cream")
# food.remove("burger")
# food.pop()
# food.insert(1, "cake")
# food.sort()
# # food.clear()
# for food in food:
#     print(food)

## 2d list
drinks = ["coffee", "soda", "milk"]
dinner = ["pizza", "hamburger", "hot dog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

print(food[0][1])

## tuple

student = ("Bro", 12, "male")

print(student.count("Bro"))
print(student.index("male"))
for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here")

## Set
utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cupboard", "knife"}

# utensils.add("napkin")
# utensils.remove("fork")

dinner_table = utensils.union(dishes)

# for x in dinner_table:
#     print(x)

print(utensils.difference(dishes))
print(utensils.intersection(dishes))


## dictionary

capital = {'USA': 'Washington DC',
           'UK': 'New York',
           'India': 'New Dehli',
           'China': 'Beijing'}
capital.update({'Germany': 'Berlin'})
capital.update({'USA': 'Las Vegas'})
capital.pop('China')
print(capital.items())
# print(capital['USA'])
print(capital.get('Germany'))
print(capital.keys())
print(capital.values())
print(capital.items())

for k, v in capital.items():
    print(k + "  \t" + v)

## index operator
name = "hashirama Tozo"
if name[0].islower():
    name = name.capitalize()

first_name = name[:9].upper()
last_name = name[9:].lower().strip()
last_character = name[-2]
print(first_name)
print(last_name)
print(last_character)

## function

def repeat(string, count):
    for i in range(count):
        print(string)


repeat("hello", 3)