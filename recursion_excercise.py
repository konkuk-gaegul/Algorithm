# 우주선 발사 카운트 다운
# 5 4 3 2 1 발사!!
def CountDown(n):
    
    if n == 0:
        return print('발사!!')
    else :
        print(n)
        CountDown(n-1)
        
CountDown(5)
print('--------------')
# 별 모양 출력하기
# *
# **
# ***
# ****
# *****

def Star(n):
    
    if n > 0:
        Star(n-1)
        print('*'*n)
    
Star(5)
print('--------------')
