#01
# N = int(input())
# M = input()
# number_list = list(map(int,M))
# sum = 0
# for i in number_list:
#     sum += i
# print(sum)

#02
n = int(input())
m = map(int, input().split())
max_m = max(m)
sum =0
result = [(i/max_m*100)for i in m]
for num in result:
    sum += num
output = sum/n
print(output)

#02
# n = int(input())
# m = map(int, input().split())
# max_m = max(m)
# sum = 0
# for num in m:
#     sum += num
# print(sum*100/max_m/n)
# 둘 다 0.0 나옴

#02 답안
# n = input()
# my_list = list(map(int, input().split()))
# my_max = max(my_list)
# sum = sum(my_list)
# print(sum * 100 /my_max/int(n))

#03 구간합
import sys
input = sys.stdin.readline

su_num, q_num = list(map(int, input().split()))
numbers = list(map(int, input().split()))

prefix_sum = [0]
#이 리스트는 numbers 리스트의 각 위치까지의 누적 합을 저장하는 역할을 합니다.temp = 0

for i in numbers:
    temp = temp + i
    prefix_sum.append(temp)
#temp에 1이 더해져서 temp는 1이 되고, prefix_sum은 [0, 1]이 됩니다.
#temp에 2가 더해져서 temp는 3이 되고, prefix_sum은 [0, 1, 3]이 됩니다.
#temp에 3이 더해져서 temp는 6이 되고, prefix_sum은 [0, 1, 3, 6]이 됩니다.
#만약 append 없이 반복문에서 바로 결과값을 뽑아내면, 반복이 끝난 후의 temp 값이 최종 결과가 됩니다.
#누적의 합을 사용하고 싶으면 append를 쓰자

for i in range(q_num):
    s, e = map(int,input().split())

print(prefix_sum[e] - prefix_sum[s-1])