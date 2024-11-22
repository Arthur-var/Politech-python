# TODO решите задачу
def task() -> float:
    with open('input.json', "r") as f:
        a = f.readlines()

        lst = list()
        dt = dict()

        for line in a:
            if '{' in line:
                dt = dict()
            elif '}' in line:
                lst.append(dt)
            key = str()
            value = str()
            flag = False

            for i in range(len(line)):
                if line[i] == '"' and not flag:
                    flag = True
                elif flag and line[i] != '"':
                    key += line[i]
                elif flag and line[i] == '"':
                    flag = False
                elif not flag and (line[i].isdigit() or line[i] == '.'):
                    value += line[i]
                elif not flag and (line[i] == ',' or line[i] == '\n'):
                    if key != '':
                        dt[key] = value
                    key = ''
                    value = ''
    amount = 0
    for d in lst:
        amount += float(d['score']) * float(d['weight'])
    return amount


print(round(task(), 3))
