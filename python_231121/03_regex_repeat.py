from regex_check import match_check

# 별 앞의 문자가 0부터 무한대까지 반복가능한..
match_check("go*d", "gd") #o가 0번이어도 true인거져..
match_check("go*d","god")
match_check("go*d", "goooooooood")

# + 앞의 문자가 최소 1번 부터 무한대
match_check("go+d", "gd") #f
match_check("go+d", "god")
match_check("go+d", "gooooood")

match_check("g[A-Z]+d", "goooooooooooood") #f 대문자는 한번도 안 나왔으니께...
match_check("g[A-Z]+d", "gOOOOOOOOOOOOd")

match_check('g[A-Z]+d', 'gABCd') # T
match_check('g[A-Z]+d', 'gAaBbCd') # F 엄격하게 A-Z만 한번 이상이라고 보면 됨.. 이 외에는 허용하지 않는다.. 좀 헷갈리는데 소문자가 섞이면 안 되지..
match_check('g[A-Z]+d', 'gAaBBbCd') # F