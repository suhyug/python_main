names = input().split()

# names_dict = {i : names_dict.get(i,0) + 1 for i in names}
names_dict = {}
# 1. names를 반복해서 names_dict를 채워나간다.
# 1-1. names_dict에 이름이 있으면 +1, 없으면 1
for i in names:
    if i in names_dict:
        names_dict[i] += 1
    else:
        names_dict[i] = 1
        #이렇게 하면 names_dict에는 각 이름과 해당 이름의 출현 횟수가 저장되어 있게 됨..

names_set = set()
# 2. names_dict를 반복해서 key, value를 가지고
# 2-1. value가 2 이상이면 names_set에 추가
for k, v in names_dict.items():
    #딕셔너리 자료형에서 키(key)와 값(value)을 함께 가져오는 형태의 for 루프는 매우 일반적이다.
    #이 방식을 사용하면 딕셔너리의 각 항목을 쉽게 순회하면서 키와 값에 동시에 접근할 수 있습니다.
    #또한 키와 값의 연관성을 더 쉽게 이해할 수 있다..
    if v >= 2:
        names_set.add(k)
        #2번 이상 출현한 이름을 담을 것..

# 3. names_set 출력
print(names_dict)
#{'유재석':2, '박명수':2}
print(names_set)
#{'유재석', '박명수'}