class Node:
    def __init__(self):
        self.data = None
        self.link = None


def printNodes(start_node):
    current = start_node

    if current == None:
        return

    print(current.data, end=' ')

    while current.link != None: # is not Node = ! = Node
        current = current.link
        print(current.data, end=' ')

    print()

def inserNone(findData, inserData):
    global memory, head, current, pre
    current = head
    if current.data == findData:
        node =Node()
        node.data = inserData
        node.link = head
        head = node
        return

    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            node = None()
            node.data = inserData
            node.link = head
            head = node
            return

    node = Node()
    node.data = inserData
    current.link = node

# 전역 변수 선언
memory = []
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']


if __name__ == "__main__":

    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()

        node.data = data
        pre.link = node
        memory.append(node)

    printNodes(head)

    inserNone("다현", "화사")
    printNodes(head)
    inserNone("사나", "다현")
    printNodes(head)
    inserNone("재남", "문별")
    printNodes(head)
