n, m, q = map(int, input().split())
a = {}
end_list = []

def disable(*args):
    if ent_list[2] in a[ent_list[1]]:
        a[ent_list[1]].remove(ent_list[2])

def reset(*args):
    a[ent_list[1]] = [j for j in range(1,m+1)]

def getmax(*args):
    sorted_a = dict(sorted(a.items(), key=lambda entry: len(entry[1]), reverse=True))
    multi_value = 1
    for key, value in sorted_a.items():
        for i_values in value:
            multi_value *= i_values

        end_list.append(key)
        break

def getmin(*args):
    sorted_a = dict(sorted(a.items(), key=lambda entry: len(entry[1])))
    multi_value = 1
    for key, value in sorted_a.items():
        for i_value in value:
            multi_value *= i_value
        end_list.append(key)
        break


for i in range(1, n+1):
    a[i] = [j for j in range(1, m+1)]

count = 0

for event in range(1, q+1):
    numbers_list = input()
    ent_list = list(map(str, numbers_list.split()))
    if len(ent_list) == 2:
        ent_list[1] = int(ent_list[1])
    if len(ent_list) == 3:
        ent_list[1] = int(ent_list[1])
        ent_list[2] = int(ent_list[2])
    if ent_list[0] == 'DISABLE':
        disable(ent_list[1],  ent_list[2], a)
    elif ent_list[0] == 'RESET':
        reset(ent_list[1])
    elif ent_list[0] == 'GETMAX':
        getmax(a)
    elif ent_list[0] == 'GETMIN':
        getmin(a)
    else:
        print('Ошибка')

for i in end_list:
    print(i)
