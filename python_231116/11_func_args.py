def hello_names(*names):
    #함수 매개변수 정의할 때 소괄호 사용
    #*(별표)names는 임의의 개수의 인자를 허용. 함수를 호출할 때 전달된 모든 값은 튜플로 묶여서 names에 전달.
    for i in names:
        print(f'안녕하세요! {i}님, 수강생분들 중에 제일 잘하세요!')

hello_names('강민서', '강은영', '권보경', '박종섭', '박준영', '서유경', '신혜인', '유재현', '이지은', '정준혁', '천다영', '최아별', '최지성')