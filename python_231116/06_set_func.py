
num_set1 = set([1, 2, 3])
num_set2 = set([3, 4])
num_set2.add(5) # 요소 추가
num_set1.update(num_set2) # 세트에 다른 세트를 추가 (합집합)
print(num_set1)
#num_set1 = {1,2,3,4,5}

print(num_set2.pop())
#{3,4,5} 중 아무거나..
#리스트 자료형 pop은 맨 뒤의 요소를 반환하지만, 세트는 순서가 없는 자료기 때문에 어떤 요소가 빠질지 예측할 수 없다..
num_set2.remove(5)
print(num_set2)
#'5' 요소를 삭제해줌.. 단, 세트에 해당 요소가 없으면 에러가 나기 때문에 if-in문을 사용해서 요소가 있는지 없는지 체크하는 방법도 추천
num_set2.clear()

num_set2 = num_set1.copy()
print(len(num_set2))
#len이니까 5 반환