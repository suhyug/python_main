def hello_names(*names, count = 1):
    #12_func_args.py에서는 def hello_names(count = 1, *names): 이었음..
    #여기서 중요한 것은 디폴트 값을 가진 매개변수들은 함수 정의에서 항상 맨 뒤에 위치해야 한다는 것입니다. 
    for name in names:
        print("Hello" * count, name)

# hello_names('손흥민', '이강인', '황희찬', 2) -> 오작동
# hello_names(2, '손흥민', '이강인', '황희찬') -> 오작동
# hello_names(count = 2, '손흥민', '이강인', '황희찬') ->오작동
hello_names('손흥민', '이강인', '황희찬', count = 2)
#HelloHello 손흥민 오류 안 뜸...
hello_names('손흥민', '이강인', '황희찬')
