#더 심플함..
names = input().split()

names_dict = {}
names_set = set()

for i in names:
    if i in names_dict:
        names_dict[i] += 1
        names_set.add(i)
    else:
        names_dict[i] = 1

print(names_dict)
#{'김이나':3, '김광석':1, '김광진':1, '유나':1}
print(names_set)
#{'김이나'}