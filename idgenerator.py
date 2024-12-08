import random

pattern = "XXX-XXX-XXX-98"
x_pattern = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

id = ""
for i in pattern:
    if i == "X":
        id += random.choice(x_pattern)
    else:
        id += i

print(id)
