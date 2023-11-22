class Animal:
    # 클래스 변수
    age = 1
    name = 'unnamed'
    # 클래스 함수
    def set_name(self, data): #data에 꿀꿀이가 들어가겠지?
        self.name = data
        #파이썬에서 메서드(클래스 내의 함수)는 첫 번째 매개변수로 항상 자신을 나타내는 self를 가져야 함.
        #이를 통해 메서드는 해당 클래스의 인스턴스에 접근하고, 인스턴스 변수와 다른 메서드를 호출할 수 있습니다.
        
    # 생성자
    # 인스턴스 함수

pig = Animal()
print(pig) #<__main__.Animal object at 0x102cb5e50>

print(type(pig)) #<class '__main__.Animal'>
print(f"우리 돼지의 이름은 {pig.name}이고, 나이는 {pig.age}살입니다.")
pig.set_name("꿀꿀이") #Animal.set_name(pig, "꿀꿀이") 이름 적용됨..
print(f"우리 돼지의 이름은 {pig.name}이고, 나이는 {pig.age}살입니다.")