import time

start = time.time()

# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)
# fib(30)

end = time.time()
print("{0:0.20} sec.".format(end -start))
#시간차이를 소수점 이하 20 자리까지 표현한다는 
# {0}: 인덱스 0의 인자를 사용하라, 여기에서는 end - start 값을 사용
# :0.2f: 소수점 이하 2자리까지 표시하라는 의미