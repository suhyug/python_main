#첫째줄 자연수 하나
#두번째줄 n개 정수 받음
#세번째줄 자연수 하나
#네번째줄 m개의 수를 받음
#시간초과
#함수 호출해서 결과 출력하는게 아직 익숙하지 않은듯!!

#gpt가..
num1 = int(input())
num1_list = [int(i) for i in input().split()]
num2 = int(input())
num2_list = [int(j) for j in input().split()]

def search(list1, list2):
    for value in list2:
# list2의 각 값을 value에 할당하고 그 value값이 list1에도 있는지 확인..
# 여기서 value는 내가 지정한 변수임.. For문의 i처럼..
        if value in list1:
            print(1)
        else:
            print(0)
search(num1_list, num2_list)
#search라는 함수에 인자 두 개를 넣은거임

# num1 = int(input())
# num1_list = [int(i) for i in input().split()]
# num2 = int(input())
# num2_list = [int(j) for j in input().split()]

# def search(num1_list, num2_list):
#     for value in num1_list:
#         if value in num2_list:
#             print(1)
#         else:
#             print(0)

# search(num1_list, num2_list)


