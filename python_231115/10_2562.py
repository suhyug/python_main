#9개의 서로 다른 자연수가 주어질 때, 최댓값을 찾고 그게 몇 번째 수인지 구해라.

n_list = []
for _ in range(9):
    #9번 반복해서 사용자로부터 숫자를 받겠다
    #반복횟수에 대한 변수가 중요하지 않으니 언더스코어를 넣음
    n_list.append(int(input()))

n_max = n_list[0]
# max_index = 1
index = 1
#!!!그냥 index로 줘도 되는거 아님? 굳이 max_index는 뒤에서 안 쓰는데 왜??
#최댓값을 찾기 위해 각 요소를 검사하는 과정에서 최댓값을 가진 요소의 인덱스를 추적하기 위한 변수

for i in range(len(n_list)):
    #!!!어차피 i가 9번 돌려야된다는 걸 아는데, 굳이 왜?? 
    if n_max < n_list[i]:
        #현재까지의 최댓값 n_max보다 현재요소 n_list[i]가 더 크면 실행
        n_max = n_list[i]
        index = i + 1
print(n_max)
print(index)




#최고 심플한 버전
# n_list = [int(input()) for _ in range(9)]
#시작이 0이고 끝이 9인(0~8) 범위를 생성한다. 범위 내 요소는 상관없다.

# n_max = max(n_list)
# index = n_list.index(n_max) + 1

# print(n_max)
# print(index)
