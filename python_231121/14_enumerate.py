#enumurate는 순서가 있는 자료형(리스트, 튜플, 문자열)을 받아 각 요소와 해당 요소의 인덱스를 튜플 형태로 반환하는 이터레이터를 생성한다..


rainbow = ["빨", "주", "노", "초", "파", "남", "보"]

enum_rainbow = enumerate(rainbow)

print(enum_rainbow)
#<enumerate object at 0x000001D850F3E660>

for i in enum_rainbow:
    print(i)
#(0, '빨') 이런식으로 나옴 
#투플 형태로 반환이니께...
#이 식은 꼭 외워두기!! 

#이터레이터는 한번만 소비할 수 있다..
#모든 요소를 쇱했기 때문에 빈 리스트가 생성된다..
#다시 쓰고 싶으면, 다시 생성해서 사용해야 한다.. enum_rainbow = enumerate(rainbow)
print(list(enum_rainbow))
#[]