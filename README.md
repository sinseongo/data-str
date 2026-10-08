# 신성오 202630112

# 10 08일(5주차)
## 단순 연결 리스트의 일반 구현,응용
### 노드(Node) 클래스 정의
class Node:
    def __init__(self):
        self.data = None
        self.link = None
### 연결 리스트 순회 및 출력 함수 (printNodes)
### is not None = != None
def printNodes(start_node):
    current = start_node

    if current == None:
        return

    print(current.data, end=' ')

    while current.link != None: # is not Node = ! = Node
        current = current.link
        print(current.data, end=' ')

    print()
### 노드 삽입 함수 (inserNone)
def inserNone(findData, inserData):
    global memory, head, current, pre
    current = head
    
### 첫 번째 노드(head) 데이터가 찾는 데이터와 일치할 경우 (맨 앞 삽입)
    if current.data == findData:
        node = Node()
        node.data = inserData
        node.link = head
        head = node
        return

### 전역 변수 선언 및 메인 실행부 (__main__)
# 전역 변수 선언
memory = []
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']


if __name__ == "__main__":

### 첫 번째 노드 생성 및 head 지정
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

### 반복문과 배열을 이용한 전체 노드 생성 및 연결
    for data in dataArray[1:]:
        pre = node
        node = Node()

        node.data = data
        pre.link = node
        memory.append(node)

### 전체 리스트 출력
    printNodes(head)

### 노드 삽입 테스트
    inserNone("다현", "화사")
    printNodes(head)
    inserNone("사나", "다현")
    printNodes(head)
    inserNone("재남", "문별")
    printNodes(head)

### 리스트를 순회하며 중간 노드 탐색
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            # (학습 참고: 원본 코드의 node = None() 오타 및 중간 삽입 로직 디버깅 필요 영역)
            node = Node() 
            node.data = inserData
            node.link = head 
            head = node
            return

### 리스트 끝까지 탐색했으나 찾는 데이터가 없는 경우 (맨 뒤에 추가)
    node = Node()
    node.data = inserData
    current.link = node


# 10월 01일(4주차)
## 선형 리스트 활용
9월 24일 (4주차)
### 데이터 Swap temp를 이용해 리스트의 두 데이터 위치 교환

### 리스트 생성과 출력 append(), for, len(), range()를 이용해 리스트 생성 및 전체 출력
kakao = ["가나", "다라", "마바", "사아","자차"]
temp = kakao[4]
print(kakao)
kakao.append("삽입")
print(kakao)
kakao[4] = kakao[5]
kakao[5] = temp
temp = kakao[3]
print(kakao)
kakao[3] = kakao[4]
kakao[4] = temp
print(kakao)

### append(), for, len(), range()를 이용해 리스트 생성 및 전체 출력
kakao = []
kakao_len = len(kakao)
kakao.append("다현")
kakao.append("정연")
kakao.append("쯔위")
kakao.append("사나")
kakao.append("지효")


### 연결 리스트의 기본 구조와 삽입·삭제

for i in range(len(kakao)):
    print(kakao[i],end=', ')

# None 클래스 정의
class Node:
    def __init__(self):
        self.data = None
        self.link = None
        

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





## 9월 17일 (3주차)
### 파이썬 기본 출력과 리스트 인덱싱,임시 변수를 활용한 데이터 삽입 및 스왑 살습
---
kakao = ["가나", "다라", "마바", "사아","자차"]
print(kakao)
kakao.append(None)
print(kakao)
kakao[5] = kakao[4]
kakao[4] = None
print(kakao)
kakao[4] = kakao[3]
kakao[3] = None
print(kakao)
kakao[3] = "삽입"
print(kakao)
kakao[3] = None
print(kakao)
kakao[3] = kakao[4]
kakao[4] = None
print(kakao)
kakao[4] = kakao[5]
kakao[5] = None
print(kakao)
---

kakao = ["가나", "다라", "마바", "사아","자차"]
temp = kakap[4]
print(kakao)
kakao.append("삽입")
print(kakao)
kakao[4] = kakao[5]
kakao[5] = temp
temp = kakao[3]
print(kakao)
kakao[3] = kakao[4]
kakao[4] = temp
print(kakao)

# 9월10일 (2주차)
# h1 태그
## h2 태그
### h3 태그
...
###### h6 태그
밑줄
---
*이텔리체*
**볼드**
***이텔릭+볼드***
~~취소선~~

1. 감자
1. 옥수수
500. 배추

* 감자
* 옥수수
* 배추
    * 배추 김치
        * 신김치
```java
public class HelloWorld {
    public static void main(String[] args) {
        // 화면에 문장을 출력합니다
        System.out.println("Hello, Java!");
        
        int age = 20;
        String name = "홍길동";
        
        System.out.println(name + "의 나이는 " + age + "살입니다.");
    }
}
```py
score = 85

if score >= 80:
    print("A등급입니다.")
else:
    print("B등급 이하입니다.")
```


### 링크
[youtube 바로가기](https://www.youtube.com "youtube 바로가기")


[코드 블럭](#코드-블럭 "코드블럭 예제")

![깃 로고](./image.png "git logo")