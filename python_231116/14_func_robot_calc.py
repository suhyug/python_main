    
def plus(a, b):
    return a + b
def minus(a, b):
    return a - b

def robot(calc_func):
    print("삐리리-삐빅! 로봇계산기입니다.")
    num1 = int(input("첫번째 숫자를 입력하세요"))
    num2 = int(input("두번째 숫자를 입력하세요"))
    print("치지직.. 삐빅!!! 삐빅!!!")
    result = calc_func(num1, num2)
    #주어진 함수 calc_func에 num1과 num2를 전달하여 함수를 호출
    #result = plus(num1, num2) 혹은 minus(num1, num2)와 동일한 역할
    print("휴... 계산 결과는요...")
    print(f"{result} 입니다. 삐빅삐빅!")

robot(plus)
#robot을 호출할 때 plus를 인자로 전달했기 때문에, calc_func 매개변수에는 실제로 plus 함수가 전달됩니다. 
robot(minus)