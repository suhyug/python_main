#딕셔너리에서 쓰는 기능
son_dict = {
    'name': '손흥민',
    'age': 29,
    'address': ['대한민국', '영국', '독일']
}

print(son_dict.keys()) # key만을 모아서 반환
print(son_dict.values()) # value만을 모아서 반환
print(son_dict.items()) # key와 value를 튜플로 묶어서 반환

print(son_dict.get('name')) # 키가 name인 value 반환
print(son_dict.get('job')) # 키가 job인 value 반환(없어서 None)
print(son_dict.get('job', '모름')) #  첫 번째 인자는 찾고자 하는 키('job'), 두 번째 인자는 해당 키가 존재하지 않을 경우 반환할 기본값('무직')입니다.
#
print('address' in son_dict) # 키 address 존재 유무

for k, v in son_dict.items():
    print(f"Key : {k}, Value: {v}")
    #Key : name, Value: 손흥민
    #Key : age, Value: 29
    #Key : address, Value: ['대한민국', '영국', '독일']
    
son_dict.clear()
print(son_dict)