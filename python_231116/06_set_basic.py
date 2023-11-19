empty_set = set()

num_set1 = set([1, 2, 3, 4, 5])
num_set2 = set([2, 4, 3, 5, 1])
#{1, 2, 3, 4, 5}
#세트는 알아서 정렬해줌

print(empty_set)
print(num_set1, num_set2)
print(num_set1 == num_set2)

str_set = set("Python is Easy")
#문자열은 불변 자료형이긴 하지만, 문자열의 길이에 따라 해시 함수가 다르게 적용되기 때문에 순서를 보장하지 않습니다. 문자열은 해시 함수의 결과가 불안정하게 나올 수 있기 때문입니다.
#{' ', 'o', 't', 'y', 's', 'h', 'a', 'E', 'i', 'n', 'P'} / 매번 다름
#그래서 sorted 쓰는구나
print(str_set)