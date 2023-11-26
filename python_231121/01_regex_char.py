from regex_check import match_check

#[하나라도 갖고 있어라..]
match_check("[abc]", "alphabet")
match_check("[abc]", "computer")
match_check("[abc]", "smart")

match_check("[0-9]", '123')
#괄호 안에 ^은 not이다..
match_check("[^0-9]", '123') #false

match_check("[a-z]", "Alphabet")
match_check("[^a-zA-Z]", "Alphabet") #false


match_check("[a-zA-Z0-9]","Gildong123")
match_check("[^a-zA-Z0-9]","Gildong123") #false
match_check("[\s]", "Hello World")

#모든 한글은 가-힣 범위 중요!!
match_check("[가-힣]", "홍길동")