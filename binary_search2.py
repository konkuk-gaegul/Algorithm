import random
## 이진 검색!!
## 함수
def binSearch(ary, fData) :
    pos = -1
    start = 0
    end = len(ary) - 1               # 마지막 인덱스
    
    while start <= end:
        mid = (start + end) // 2
        if fData == ary[mid]:        # 찾는 게 배열의 중앙값인가?
            return mid               # 맞다면 중앙의 인덱스 리턴
        elif fData > ary[mid]:       # 찾는 게 중앙값보다 큰가?
            start = mid + 1          # 중앙 인덱스+1을 시작으로
        else :                       # 찾는 게 중앙값보다 작다면
            end = mid - 1            # 중앙 인덱스-1을 끝으로..
    
    return pos

## 전역
dataAry = [ random.randint(1, 999) for _ in range(50)]
findData = dataAry[random.randint(0, 49) ]
dataAry.sort()      # 오름차순으로 정렬!

## 메인
print('배열 -->', dataAry)
position = binSearch(dataAry, findData)
if position == -1:
    print(findData, '없어요 ㅠㅠ')
else:
    print(findData, '는', position, '위치에 있다.')