# TODO решите задачу
def task() -> float:
    amount = 0
    score = 0
    weight = 0
    with open("input.json", 'r') as f:
        a = f.readlines()
    for i in range(len(a)):
        if a[i].find("score") != -1:
            score = float(a[i][((a[i].find("score")) + 8):len(a[i]) - 2])
        elif (a[i].find("weight")) != -1:
            weight = float(a[i][((a[i].find("weight")) + 9):len(a[i]) - 1])
        if (score != 0) and (weight != 0):
            amount += score * weight
            score, weight = 0, 0
    return round(amount, 3)


print(task())
