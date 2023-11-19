# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다.
#이때, A에서 X보다 작은 수를 모두 출력해라

# N, X = [int(i) for i in input().split()]
N, X = map(int, input().split())
# 공백으로 구분된 정수를 받아 각 N과 X에 할당하는 역할
#리스트 컴프리헨션 : 간결하게 리스트를 생성하는 파이썬 기능 중 하나

A = [int(i) for i in input().split()]
# A = int(input().split())
# A에 리스트가 아닌 정수 하나만 저장되고 있습니다. 
# 따라서 A를 리스트로 변환해주어야 합니다.

# A 안에서 X보다 작은 수를 결과물로 출력
result = [i for i in A if i < X]

print(*result)
#[1,4,2,3]가 별 붙이면 그냥 1 4 2 3 으로 나옴. 문제의 예제 출력 예시랑 똑같이..
# spread operator인 *을 사용하면,
# 리스트의 요소를 unpacking해서 출력할 수 있습니다.