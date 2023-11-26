from regex_check import match_check

#여기서 정규표현식 앞에 있는 문자는 식이라고보고, 이미 쓰여있는 문자로 계산하지 말 것..
#{}는 반복횟수
match_check("hel{2}o", "hello") #true

match_check("hel{1,3}","heo") #f
match_check("hel{1,3}","helo")
match_check("hel{1,3}","hello")
match_check("hel{1,3}","helllo")
match_check("hel{1,3}","hellllo") #f

#물음표는 무조건 반복{0,1}
#정규표현식 앞의 문자 빼고 나머지는 고정임 즉, helo는 고정인 채로 계산을 해야됨..
match_check("hell?o","helo") #이 경우에 l은 0임
match_check("hell?o","hello") #이 경우에 l은 1임
match_check("hell?o","helllo") #이 경우에 l은 2이기 때문에 False

match_check("hel{,3}o", "heo") #true 3이하니까 0도 가능한가보다..
match_check("hel{,3}o", "helo")
match_check("hel{,3}o", "hello")
match_check("hel{,3}o", "helllo")
match_check("hel{,3}o", "hellllo") #f

match_check("hel{3,}o", "hello") #f
match_check("hel{3,}o", "helllo")
match_check("hel{3,}o", "hellllo")

match_check("go{0,}d", "gd")
match_check("go{1,}d", "gd") #f