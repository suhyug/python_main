#정확히 조건, 문제가 뭔지 몰겠음..
X = int(input())
A = [int(i) for i in input().split()]

for i in range(len(A)) :
    #기본적으로 range 인자에 하나만 넣으면 i는 0부터지만, for i in range(start, stop, step): 이런식으로 작성 가능하다.
    if A[i] >= X :
        del A[i]

# 반복문이 동작하면서 배열의 크기가 변경되면 정상적인 반복이 불가능할 수 있다.

#적절하게 작성한다면..
X = int(input())
A = [int(i) for i in input().split()]

for i in range(len(A)-1, -1, -1):
    if A[i] >= X:
        del A[i]

print(A)
