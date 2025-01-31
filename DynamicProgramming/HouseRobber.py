def HouseRobber(hval):
    valArr = [hval[0], max(hval[1], hval[0])]
    for i in range(2, len(hval)):
        val1 = valArr[i - 1]
        val2 = valArr[i - 2] + hval[i]
        if val1 > val2:
            valArr.append(val1)
        else:
            valArr.append(val2)
        print(valArr)
    return valArr[-1]

sol = HouseRobber([6, 7, 1, 3, 8, 2, 4])
print(sol)