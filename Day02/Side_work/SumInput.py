from functools import reduce


def sum_numbers():
    try:
        number = [int(x.strip()) for x in input("Enter a list number: ").split(",")]
        return sum(number)
    except ValueError as e:
        print("❌ Please enter only numbers separated by commas.")

print(sum_numbers())