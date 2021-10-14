check1 = []
check2 = []
try:
    def rohanDasTable():
        tableOf = int(input("Enter the number whose table you want to know : "))
        import random
        randomVal = random.randint(6, 9)
        for i in range(1, 11):
            answer = tableOf * i
            if i == randomVal:
                answer += 2
            check1.append(answer)
            print(str(answer))


    def isCoorect():
        rohanDasTable()
        tableOf = int(input("Enter the number whose table you want to check >>>  "))
        for i in range(1, 11):
            answer = tableOf * i
            check2.append(answer)
            print(str(answer))

    isCoorect()

    for i in range(0, 10):
        if check1[i] != check2[i]:
            print(f" At number {i+1} the table is wrong")
        else:
            print("The table is correct")

except Exception as e:
    print(e)
