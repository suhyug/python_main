import sys

sys.stdin.readline()
#여기서 N변수를 쓰지 않을 거니까, 변수 선언 생략해도 됨..
nums = sys.stdin.readline().rstrip()

result = 0
for i in nums:
    result += int(i)
print(result)