import random
## 함수
def findMinIndex(ary):
    minIdx = 0          # 0번 인덱스를 가장 작은 값으로 가정
    for  i in range(1, len(ary)):
        if ary[minIdx] > ary[i]:
            minIdx = i
    return minIdx

## 전역
# testAry = [55, 88, 33, 77]
testAry = [random.randint(1, 99) for _ in range(20) ]

## 메인
print(testAry)
minPos = findMinIndex(testAry)
print('최소값 :', testAry[minPos])