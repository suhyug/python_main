def hello_names(**msg):
    #함수의 매개변수에서 사용되어, 키워드 인자들을 딕셔너리로 묶습니다.
    #딕셔너리 형태가 아니면, 오류 발생!!
    #이러한 매개변수를 "키워드 가변 인자"라고 부릅니다.
    for i in msg:
        print(f"{msg[i]}! {i}")
        # print(msg[i] + "! " + i)
        #프린트 형식, 포매팅 아직 헷갈림..
        

hello_names(최인규 = "안녕하세요", Steve = "Hello", 다나카 = "곤니치와")