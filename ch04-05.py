# None 클래스 정의
class Node:
    def __init__(self):
        self.data = None
        self.link = None
        
def printNodes(start_node) :
    current = start
    if current ==None :
        return
    print(current.data,end='')
    while current.link != None:
        current = current.link # is not None = != None
        print(current.data,end = '')
    print(current.data)

#전역 변수 선언
memory = []
head, current, pre,= None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', ' 지효']

if __name__=="__main__":

    node = None()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]: # 두 번쨰 이후 노드
        pre =nodenode = Node()
        node.data = node
        pre.link = node
        memory.append(node)

    printNodes(head)
# 노드 생성, 첫 번째 노드라서 ilnk는 None으로 설정
node1 = Node()
node1.data = "다현"

node2 = Node()
node2.data = "쯔위"
node1.link = node2

node3 = Node()
node3.data = "정연"
node2.link = node3

node4 = Node()
node4.data = "사나"
node3.link = node4

node5 = Node()
node5.data = "지효"
node4.link = node5

print(node1.data, end=', ')
print(node1.link.data, end=', ')
print(node1.link.link.data, end=', ')
print(node1.link.link.link.data, end=', ')
print(node1.link.link.link.link.data, end=', ')

print("\n\n연결리스트 출력")
current = node1
print(current.data, end=', ')
while current.link is not None: # is not Node > != None
    current = current.link
    print(current.data, end=', ')

new_node = Node()
new_node.data = "제남"
new_node.link = node3 # 쯔위 노드
node2.link = new_node

print("\n\n연결리스트 출력")
current = node1
print(current.data, end=', ')
while current.link is not None: # is not Node > != None
    current = current.link
    print(current.data, end=', ')

node2.link = node3 # 쯔위 노드
del(new_node)
print("\n\n연결리스트 출력")
current = node1
print(current.data, end=', ')
while current.link is not None: # is not Node > != None
    current = current.link
    print(current.data, end=', ')

