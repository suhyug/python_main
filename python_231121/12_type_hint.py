#Type Hinting
def is_even(num : int) -> bool:
    # 함수의 이름은 is_even이고, 정수형 매개변수 num을 받습니다. 
    # -> bool은 함수가 부울(boolean) 값을 반환한다는 것을 나타냅니다.
    if num % 2 == 0:
        return True
    else:
        return False
    
print(is_even(1)) #f
print(is_even(2)) #t
#type hint 가 틀려도 오류는 안 나지만... 지양하자
#mypy로 오류를 잡아주긴한다..

#def is_even(num: int) -> bool:
#     return num % 2 == 0
# print(is_even(1))  # False
# print(is_even(2))  # True
# num % 2 == 0 자체가 불리언 값이므로, 추가적인 if 문 없이 그 결과를 그대로 반환할 수 있다..
