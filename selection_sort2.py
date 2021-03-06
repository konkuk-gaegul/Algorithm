import random
## 함수
def selectionSort(ary):
    n = len(ary)
    for cy in range(0, n-1):
        minIdx = cy         # 매 싸이클마다 첫 번째 요소를 가장 작은 값의 인덱스
        for i in range(cy+1 , n):
            if ary[minIdx] > ary[i]:
                minIdx = i
        ary[cy], ary[minIdx] = ary[minIdx], ary[cy]
    return ary

## 전역
dataAry = [ random.randint(10, 99) for _ in range(20)]

## 메인
print('정렬 전 -->', dataAry)
dataAry = selectionSort(dataAry)
print('정렬 후 -->', dataAry)

# n   4
# cy  0, 1, 2

# i   1, 2, 3 when cy = 0
# i   2, 3    when cy = 1
# i   3       when cy = 2
