def getLCString(str1,str2):
    li = []
    long = str1 if len(str1) > len(str2) else str2
    short = str2 if str1 == long else str1
    for i in range(len(short)):
        for j in range(len(short),0,-1):
            if long.find(short[i:j]) != -1:
                if not li:
                    li.append(short[i:j])
                if len(li[0])<len(short[i:j]):
                    li[0] = short[i:j]
    return li[0]

print(getLCString('afsdgfdvcchdfg','advcdddd'))

