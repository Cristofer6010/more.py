import random

names1 = []
names2 = []
names3 = []
try:
    numberOfTimes = int(input("Enter how many names you want to jumble : "))
    for i in range(1, numberOfTimes+1):
        name = input(f"Enter {i} name : ")
        parts = name.split(" ")
        if str(parts[0]) in name:
            names1.append(str(parts[0]))
        if str(parts[1]) in name:
            names2.append(str(parts[1]))
    for j in range(0, numberOfTimes):
        randomValue = random.choice(names2)
        names3.append(names1[j] + " " + randomValue)
        names2.remove(randomValue)
except Exception as e:
    print(e)
print(names3)
