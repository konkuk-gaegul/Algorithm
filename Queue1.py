## 함수


## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

## 메인
# enQueue
rear += 1
queue[rear] = '화사'

rear += 1
queue[rear] = '솔라'

rear += 1
queue[rear] = '문별'

print('출구 <--', queue, '<--입구')

# deQueue
front += 1              # 특정 요소가 나오는 게 아니라
data = queue[front]     # 맨 앞의 요소가 나오게 한다
queue[front] = None     # 나온 자리는 다시 None 삽입
print('식사 손님 :', data)

front += 1
data = queue[front]
queue[front] = None
print('식사 손님 :', data)

front += 1
data = queue[front]
queue[front] = None
print('식사 손님 :', data)

print('출구 <--', queue, '<--입구')




# while True:
#     rear += 1
#     queue[rear] = 'friend'