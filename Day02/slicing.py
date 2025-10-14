name = "Hashirama Hanzo"

first_name = name[:9]
last_name = name[10:]
funky_name = name[::2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

website = "https://google.com"

slice = slice(8, -4)
print(website[slice])