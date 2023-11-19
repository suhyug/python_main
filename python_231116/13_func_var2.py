def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

calc_list = [plus, minus]
print(calc_list[0](5, 6))
print(calc_list[1](17, 1))
#함수를 리스트에 담아서 사용할 수 있음!

calc_dict = {'더하기' : plus, '빼기' : minus}
#딕셔너리 형태로 함수를 담아서 사용할 때는 인덱스로 뽑을 수 없으니 반드시 키값으로 뽑아내야 한다!!
print(calc_dict['더하기'](10, 10))
print(calc_dict['빼기'](43, 20))