import re

# c_obj = re.compile('[a-z]+') => re.compile() 함수를 사용하여 정규표현식 패턴 [a-z]+를 컴파일한 객체를 생성, 이 정규표현식은 소문자 알파벳이 최소 1회 이상 반복되는 패턴을 의미
# match_obj =  c_obj.match("pyth0n") =>c_obj에 저장된 정규표현식 객체를 사용하여, 주어진 문자열 "pyth0n"과 매치되는지 확인, match() 메서드는 문자열의 시작에서부터 정규표현식과 매치되는지 확인하며, 매치된 경우에는 매치 객체를 반환. 만약 매치되지 않으면 None을 반환합니다.

#밑에것처럼 간단하게 작성 가능..

match_obj = re.match('[a-z]+', 'pyth0n')


print(match_obj) #<re.Match object; span=(0, 4), match='pyth'>
print(match_obj.group()) #pyth =>매치된 부분 문자열을 반환
print(match_obj.start()) #0 =>매치된 부분 문자열의 시작 인덱스
print(match_obj.end()) #4 해당 문자열의 끝 다음 인덱스를 반환하니께 3이 아니라 4
print(match_obj.span()) #(0,4) =>매치된 부분 문자열의 시작과 끝 인덱스를 튜플로 반환