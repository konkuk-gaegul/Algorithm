# https://cafe.naver.com/algorystudy

class Node():
    def __init__(self):
        self.data = None
        self.link = None
        
def printNodes(start):
    current = start
    print(current.data , end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

# 전역 변수
head, current, pre = None, None, None
memory = []
dataArray = ['다현', '정연', '쯔위' ,'사나', '지효']

# 메인
node = Node() # 첫 노드
node.data = dataArray[0]
head = node
memory.append(node)

for data in dataArray[1:]: # ['정연', '쯔위' ,'사나', '지효']
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)
    
printNodes(head)
