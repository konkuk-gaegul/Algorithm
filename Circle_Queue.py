## 함수
def isQueueFull():
    global SiZE, queue, front, rear
    if (rear + 1) % SIZE == front:
        return True
    else :
        return False
    
def enQueue(data):
    global SiZE, queue, front, rear
    if isQueueFull() :
        print('큐 꽉!')
        return
    else :
        rear = (rear + 1) % SIZE
        queue[rear] = data

def isQueueEmpty():
    global SiZE, queue, front, rear
    if front == rear:
        print('큐가 비었습니다.')
        return True
    else :
        return False
    
def deQueue() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print('큐가 비었다.')
        return None
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SiZE, queue, front, rear
    if isQueueEmpty() :
        print('큐가 텅 비었습니다.')
        return None
    return queue[(front + 1) % SIZE]

## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = 0

## 메인
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')
print('출구 <--', queue, '<--입구')
print(peek())