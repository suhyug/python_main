#세트는 주로 중복을 방지하여, 교집합/합집합/차집합 구할 때 씀
# my_set1 = set([1,2,3,4,5,6])
# my_set2 = set([4,5,6,7,8,9])
my_set1 = {1,2,3,4,5,6}
my_set2 = {4,5,6,7,8,9}
#둘 다 표현 가능한..

# 합집합
# print(my_set1 | my_set2)
# print(my_set1.union(my_set2))
# my_set1.update(my_set2)
# print(my_set1)

# 교집합
print(my_set1 & my_set2)
print(my_set1.intersection(my_set2))
# my_set1.intersection_update(my_set2)
# my_set1과 my_set2의 교집합을 구하고, 그 결과를 my_set1에 저장
# print(my_set1)

# 차집합
print(my_set1 - my_set2)
print(my_set1.difference(my_set2))
# my_set1.difference_update(my_set2)
# print(my_set1)

# 대칭차집합
#두 세트에 공통으로 속하지 않는 요소만
print(my_set1 ^ my_set2)
print(my_set1.symmetric_difference(my_set2))
#{1, 2, 3, 7, 8, 9}
my_set1.symmetric_difference_update(my_set2)
print(my_set1)
#{1, 2, 3, 7, 8, 9}