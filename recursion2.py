## 재귀를 통한 숫자 합계 내기
## 1부터 10까지 더해보자

## 함수
def addNumber(num):
    if num <= 1:
        return 1
    
    else:
        return num + addNumber(num-1)

## 메인

print(addNumber(10))
