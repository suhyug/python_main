from regex_check import match_check

#점은 \n을 제외한 모든 문자 그만큼 점의 개수가 중요
match_check("a.b","a0b")
match_check("a.b","a.b")
match_check("a.b","aaab") #true임 뒤쪽 a'aab'
match_check("a.b","a\nb") #f
match_check("a.b","a\tb") 
match_check("a.b","a   b") #f 점은 하나이니까 틀리죠
match_check("a.b","a b")
match_check("a.b","acb") 
match_check("a.b","a\n\tb") #f

#[.] 괄호 안의 문자 그대로 점이 있어야겠죠
match_check("a[.]b","a.b") 
match_check("a[.]b","a0b") #f
match_check("a[.]b","a\nb") #f










