import sys

# 함수를 변수에 할당하고 사용할 수 있다.
new_input = sys.stdin.readline 
#sys 모듈의 stdin 객체를 사용하여 표준 입력에서 한 줄을 읽어오는 메서드입니다.
#대부분의 경우에는 input() 함수를 사용해도 충분하며, sys.stdin.readline()은 대량의 입력을 처리할 때 성능상의 이점이 있을 때 사용

data = new_input()
print(data)