import random

# Using the fact that the numbers are either different or not
# to add either 1 or 0 the sum, then dividing by the count

n = int(1e7)
s = 0

for i in range(n):
    if len({random.randint(0, 9),
         random.randint(0, 9),
         random.randint(0, 9),
         random.randint(0, 9),
         random.randint(0, 9),
         random.randint(0, 9),
         random.randint(0, 9),
         random.randint(0, 9)}) == 8:
        s += 1

prob = s/n*100
print(f"Probability: {prob:.5f} %")
# Prints about:
# Probability: 1.80593 %
