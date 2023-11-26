import re

match_obj = re.search('(\w+)\s+([0,1]{3}[-]\d{4}[-]\d{4})', "홍길동 010-1234-1234")
#\w [a-zA-Z0-9] \s 스페이스  0,1숫자조합 세자리 하이픈 필수 \d[0-9]
#근데 어떻게 한글을 뽑아냈을까??

print(match_obj) #<re.Match object; span=(0, 17), match='홍길동 010-1234-1234'>

print(match_obj.group(0)) #매칭된 문자열 전체 출력 홍길동 010-1234-1234
print(match_obj.group(1)) #그룹 1 출력 홍길동
print(match_obj.group(2)) #그룹 2 출력 010-1234-1234

