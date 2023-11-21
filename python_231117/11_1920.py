
def get_num_list():
    int(input())
    #하나의 값을 입력받는 인풋
    return [int(i) for i in input().split()]
    #여러개의 값을 입력받는 인풋
    #i는 리스트의 각 요소를 차례로 지칭..

n_list = get_num_list()
m_list = get_num_list()
#각각 하나씩 뽑아야되니께..

def search_num(n_list, m_list):
    for i in m_list:
        print(int(i in n_list))
        #i in n_list 이 조건식은 인덱스를 반환하는 것이 아니라 값의 존재 여부를 판단
        #i가 n_list에 속한다면 이는 참(True)을 나타내므로 int(True)는 1
        #반대로, i가 n_list에 속하지 않는다면 이는 거짓(False)을 나타내므로 int(False)는 0
        #여기에 int를 넣어줌으로써 True, False값을 정수로 변환해서 1, 0으로 나옴...

search_num(n_list, m_list)