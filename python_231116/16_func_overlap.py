#average 함수 내에 length 함수와 sum 함수가 정의
#이런 함수를 "내부 함수" 또는 "지역 함수"라고 부른다.
#이들은 average 함수 내부에서만 사용 가능하며, 외부에서는 직접적으로 호출할 수 없다.

def average(*scores):
    #별표로 임의의 개수의 인자를 받을 수 있다!
    def length():
        return len(scores)
    # 몇 개의 인자를 받았는지를 알아야 평균을 낼 수 있으니께..
    def sum():
        total = 0
        #다 더한 값을 넣어줄 바구니
        for i in scores:
            #scores의 모든 요소를 더한 값을 구하는 방법
            total += i
        return total
    
    return sum() / length()
    #함수말고 값으로 치면, total/len(scores)가 되는 것임!
    #각 함수에서 리턴한 값이 중요한 거임!
    
print(average(10,20,30,40,50))