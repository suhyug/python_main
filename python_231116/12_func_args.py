def hello_names(count = 1, *names):
    for name in names:
        print("Hello" * count, name)

# hello_names('김석우', '차학연', '김선호', 2)
#오류

# hello_names(2, '김석우', '차학연', '김선호')
#HelloHello 김석우

# hello_names(count = 2, '김석우', '차학연', '김선호')
# hello_names(count = 2, names = ('김석우', '차학연', '김선호'))
# 오류
#위의 식이 count에 숫자 2 외에도 '김석우', '차학연', '김선호'를 인자로 받아서 문제가 생기는거?
# 그러면 names=에 따로 값을 주면 돼야 되는 거 아님??
 
#count=2는 키워드 인자이므로 맨 앞에 있는 디폴트 값을 가진 매개변수에 값을 전달할 수 있습니다. 
#그러나 '김석우', '차학연', '김선호'는 위치 인자이므로 디폴트 값을 가진 매개변수에 값을 전달할 수 없어서 오류 발생!

# hello_names('김석우', '차학연', '김선호', count = 2)
#오류

# hello_names('김석우', '차학연', '김선호')
#오류

hello_names(2,'김석우', '차학연', '김선호')
#HelloHello 김석우
#오류는 아닌데...
