katalk = []

# add_data 함수의 변수로 friend 설정
def add_data(friend):

  katalk.append(None)   # 마지막 인덱스에 빈 문자열 추가
  
  katalk[-1] = friend   # 그 빈 문자에 추가할 친구 삽입
  
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
add_data('모모')


def insert_data(position, friend):
    katalk.append(None)
    kLen = len(katalk)

    for i in range(kLen-1, position, -1):
        katalk[i] = katalk[i-1]
        katalk[i-1] = None

    katalk[position] = friend
        
insert_data(3, '미나')
  
def delete_data(position):
      
    katalk[position] = None

    kLen = len(katalk)

    for i in range(position+1, kLen, 1):
        katalk[i-1] = katalk[i]
        katalk[i] = None

    del(katalk[kLen-1])
    
delete_data(4)
print(katalk)