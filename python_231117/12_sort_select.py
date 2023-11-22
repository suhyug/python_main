#선택 정렬 알고리즘 구현 : 주어진 리스트에서 가장 작은 값을 찾아 맨 앞으로 옮기는 작업을 반복/정렬

def selection_sorted(list):
    for i in range(len(list)-1):
        min = i
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                min = j
        list[i], list[min] = list[min], list[i] # 스왑
        # print(list)
    return list

chars = ['b', 'c', 'd', 'e', 'a']
print(selection_sorted(chars))