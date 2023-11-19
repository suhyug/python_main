#함수
def hello1():
    print("Hello")
    
def hello2(name):
    #parameter = 매개변수
    print(f"Hello~ {name}")

def hello3(name, count):
    for _ in range(count):
        #0부터 시작해서 1씩 증가하는 값을 count 번 반복한다
        #즉, 0,1,2를 생성하고 이 세 값에 대해 루프를 돈다..
        print(f"Hello! {name}")

hello1()
hello2("Kim")
hello3("Lee", 3)