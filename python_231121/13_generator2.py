#range함수가 대표적으로 제너레이터다....

def get_many_type_data():
    while True:
        yield 1
        yield '문자열'
        yield True

type_generator = get_many_type_data()

for i in range(5):
    print(next(type_generator))
    #next() 함수를 호출하면 제너레이터 함수가 다음 yield 문에서 멈추고
    #해당 yield 문에서 반환한 값이 next() 함수의 반환값으로 전달 
    #그리고 다음 yield 문부터 제너레이터 함수가 계속 실행
    
#1
#문자열
#True
#1
#문자열