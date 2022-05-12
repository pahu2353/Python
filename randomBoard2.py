import random
sum = 0

# lazy cypress kouri way
for i in range(10):
    for j in range(10):
        x = random.randint(0, 9)
        sum += x
        print (x, end = ' ') # makes it print on one line
    print()

print("Sum =", sum)