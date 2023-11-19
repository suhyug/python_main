def say_hello():
    nation = input("국적을 입력하세요! ---> ")
    if nation.lower() == "korea" or nation == "한국" or nation == "대한민국":
        return hello_korean()
    else :
        return hello_english()
    #return 값으로 함수를 넣을 수도 있다..

def hello_korean():
    print("안녕하세요!")

def hello_english():
    print("Hello!")
    
say_hello()
#함수 호출을 해야지..