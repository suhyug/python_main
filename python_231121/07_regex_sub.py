import re

# re.sub(패턴, 대체문자, 대상문자)
target = 'aabbcc'
target = re.sub('[a]+',"안녕", target)
#re.sub() 함수를 사용하여 정규표현식 패턴 [a]+과 일치하는 부분을 "안녕"으로 대체합니다.
#패턴과 일치하는 부분은 aa니까 이 자리에 안녕이 들어가서 '안녕bbcc'가 됨..

print(target)