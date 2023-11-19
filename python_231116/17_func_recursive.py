#재귀적인 방식으로 주어진 값까지의 합을 구한다..
def recursion_sum(num):
    if num == 1:
        return 1
    else :
        #else: 자체를 생략 가능
        result = recursion_sum(num - 1)
        return num + result
#다섯 번째 호출의 결과인 1이 네 번째 호출의 num에 더해져서 2 반환
#네 번째 호출의 결과인 2가 세 번째 호출의 num에 더해져서 3 반환
#세 번째 호출의 결과인 3이 두 번째 호출의 num에 더해져서 4 반환
#두 번째 호출의 결과인 4가 처음 호출의 num에 더해져서 5 반환

print(recursion_sum(5))
#5+4+3+2+1 = 15