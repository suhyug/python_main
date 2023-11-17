# 애너그램 체크
#첫째줄에는 테스트 케이스의 개수, 두 단어를 비교

CASE_NUM = int(input())
#몇 개 쓸건지 개수부터 입력받는다
#상수로 사용되는 변수는 규칙으로 대문자

for _ in range(CASE_NUM):
    #각 케이스마다 두 개 단어를 입력받음
    word1, word2 = input().split()
    #for문 안에 들어와야 word1, word2를 세번 입력받을 수 있고, 세 번 다 다른값으로 판단할 수 있음..!
    if sorted(word1) == sorted(word2):
        #sorted는 반복가능한 객체의 요소를 정렬한 새로운 리스트를 반환, 정렬은 기본적으로 오름차 순
        print(f"{word1} & {word2} are anagrams.")
    else:
        print(f"{word1} & {word2} are NOT anagrams.")
        
