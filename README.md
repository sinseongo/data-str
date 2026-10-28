# 신성오 202630112
## 10월 15일

### 1. 원형 연결 리스트의 개념

원형 연결 리스트(Circular Linked List)는 마지막 노드가 첫 번째 노드와 다시 연결되는 구조이다.

단순 연결 리스트는 마지막 노드의 `link`가 `None`으로 끝나지만, 원형 연결 리스트는 `head`를 가리킨다.

#### 원형 연결 리스트 구조

```text
        ┌──────────────────────────────┐
        ↓                              │
다현 → 정연 → 쯔위 → 사나 → 지효 ──────┘
```

- `data`: 노드에 저장되는 값
- `link`: 다음 노드를 가리키는 참조
- `head`: 첫 번째 노드를 가리키는 변수
- `current`: 현재 확인하는 노드
- `pre`: 현재 노드의 이전 노드

#### 단순 연결 리스트와 차이

| 구분 | 단순 연결 리스트 | 원형 연결 리스트 |
|---|---|---|
| 마지막 노드 | `None`을 가리킴 | 첫 노드를 가리킴 |
| 형태 | 일직선 구조 | 원형 구조 |
| 순회 종료 | `None`에 도달하면 종료 | 처음 노드로 돌아오면 종료 |

### 2. Node 클래스 만들기

노드는 데이터와 다음 노드의 연결 정보를 저장한다.
`Node` 클래스로 각 노드 객체를 생성할 수 있다.

```python
class Node:
    def __init__(self):
        self.data = None
        self.link = None
```

- `__init__()`: 객체가 만들어질 때 실행되는 초기화 메서드
- `self.data`: 노드에 담을 데이터
- `self.link`: 다음 노드의 위치
- `None`: 아직 값이나 연결이 지정되지 않은 상태

### 3. 노드 하나로 원형 만들기

노드가 하나뿐이면 해당 노드가 자기 자신을 가리키도록 연결한다.

```python
node1 = Node()
node1.data = "다현"
node1.link = node1
```

- `node1 = Node()`: 새 노드 생성
- `node1.data = "다현"`: 데이터 저장
- `node1.link = node1`: 자기 자신과 연결하여 원형 구조 생성

### 4. 노드 두 개 연결하기

두 번째 노드를 추가할 때는 첫 번째 노드가 두 번째 노드를 가리키고, 두 번째 노드는 다시 첫 번째 노드를 가리키게 한다.

```python
node1 = Node()
node1.data = "다현"
node1.link = node1

node2 = Node()
node2.data = "정연"

node1.link = node2
node2.link = node1
```

- `node1.link = node2`: 첫 번째 노드와 두 번째 노드 연결
- `node2.link = node1`: 두 번째 노드에서 첫 번째 노드로 연결

### 5. 여러 노드 연결하기

데이터가 여러 개일 때도 노드를 순서대로 연결하고, 마지막 노드가 첫 번째 노드를 가리키도록 설정한다.

```python
class Node:
    def __init__(self):
        self.data = None
        self.link = None

node1 = Node()
node1.data = "다현"
node1.link = node1

node2 = Node()
node2.data = "정연"
node1.link = node2
node2.link = node1

node3 = Node()
node3.data = "쯔위"
node2.link = node3
node3.link = node1

node4 = Node()
node4.data = "사나"
node3.link = node4
node4.link = node1

node5 = Node()
node5.data = "지효"
node4.link = node5
node5.link = node1
```

각 노드는 다음 노드를 가리키며, 마지막 노드의 `link`는 첫 번째 노드인 `node1`을 가리킨다.

#### 원형 연결 리스트 순회

```python
current = node1

while True:
    print(current.data, end=" ")
    current = current.link

    if current == node1:
        break
```

- `current = node1`: 첫 번째 노드부터 시작
- `current = current.link`: 다음 노드로 이동
- `current == node1`: 처음 노드로 돌아왔는지 확인
- `break`: 한 바퀴를 돌면 반복 종료

원형 구조에서는 `current is None`을 종료 조건으로 사용하면 안 된다. 마지막 노드가 `None`이 아닌 첫 번째 노드를 가리키기 때문이다.

### 6. 중간에 노드 삽입하기

정연과 쯔위 사이에 새 노드를 넣으려면 새 노드가 기존 다음 노드를 먼저 가리키게 한 뒤, 정연의 연결을 새 노드로 바꾼다.

```python
newNode = Node()
newNode.data = "재남"

newNode.link = node2.link
node2.link = newNode
```

- `newNode.link = node2.link`: 새 노드를 기존 다음 노드와 연결
- `node2.link = newNode`: 정연 노드가 새 노드를 가리키도록 변경

새 노드의 연결을 먼저 설정해야 기존 노드와의 연결이 끊어지는 것을 막을 수 있다.

### 7. 노드 삭제하기

쯔위 노드를 삭제할 때는 이전 노드가 삭제할 노드의 다음 노드를 바로 가리키게 한다.

```python
node2.link = node3.link
del(node3)
```

- `node2.link = node3.link`: 정연이 쯔위를 건너뛰고 다음 노드를 가리킴
- `del(node3)`: `node3` 변수의 참조를 삭제

다른 곳에서 해당 객체를 참조하지 않는다면 메모리 정리 대상이 될 수 있다.

### 8. 원형 연결 리스트에 사용하는 변수

| 변수 | 역할 |
|---|---|
| `memory` | 생성한 노드 객체를 보관하는 리스트 |
| `head` | 첫 번째 노드 |
| `current` | 현재 처리하는 노드 |
| `pre` | 이전 노드 |

```python
memory = []
head, current, pre = None, None, None
```

여러 변수에 같은 값을 한 번에 대입할 수 있다. `pre`는 이전 노드를 자동으로 찾는 변수가 아니므로 코드에서 직접 지정해야 한다.

### 9. 첫 번째 노드 생성하기

배열의 첫 번째 데이터를 노드에 저장한 다음, `head`로 지정하고 자기 자신과 연결한다.

```python
class Node:
    def __init__(self):
        self.data = None
        self.link = None

memory = []
head, current, pre = None, None, None

dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

node = Node()
node.data = dataArray[0]
head = node
node.link = head
memory.append(node)
```

- `dataArray[0]`: 배열의 첫 번째 데이터
- `head = node`: 첫 번째 노드 지정
- `node.link = head`: 노드가 첫 번째 노드를 가리키도록 연결
- `memory.append(node)`: 노드 객체를 관리용 리스트에 저장

### 10. 두 번째 이후 노드 추가하기

첫 번째 노드가 만들어진 뒤에는 기존 노드를 `pre`에 저장하고, 새 노드를 생성해 연결한다.

```python
pre = node
node = Node()
node.data = data
pre.link = node
node.link = head
memory.append(node)
```

1. `pre = node`: 기존 노드를 이전 노드로 저장
2. `node = Node()`: 새 노드 생성
3. `node.data = data`: 데이터 저장
4. `pre.link = node`: 이전 노드와 새 노드 연결
5. `node.link = head`: 새 노드를 첫 번째 노드와 연결
6. `memory.append(node)`: 노드 객체 저장

첫 번째 노드는 `head`로 지정하고, 이후 노드는 이전 노드의 `link`를 이용해 이어 붙인다.

### 11. 원형 연결 리스트 생성 코드

배열의 데이터를 이용해 노드를 차례대로 만들고 연결하는 코드이다.

```python
class Node:
    def __init__(self):
        self.data = None
        self.link = None


def printNodes(start):
    if start is None:
        return

    current = start

    while True:
        print(current.data, end=" ")
        current = current.link

        if current == start:
            break

    print()


memory = []
head, current, pre = None, None, None

dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

if __name__ == "__main__":
    node = Node()
    node.data = dataArray[0]
    head = node
    node.link = head
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)

    printNodes(head)
```

- `dataArray[1:]`: 첫 번째 데이터를 제외한 나머지 데이터
- `pre.link = node`: 이전 노드와 새 노드 연결
- `node.link = head`: 새 노드가 첫 번째 노드를 가리키도록 설정
- `printNodes(head)`: 첫 노드부터 원형 리스트 순회

### 12. 원형 연결 리스트 순회 함수

원형 연결 리스트는 처음 노드로 돌아왔을 때 반복을 끝내도록 조건을 설정한다.

```python
def printNodes(head):
    if head is None:
        return

    current = head

    while True:
        print(current.data, end=" ")
        current = current.link

        if current == head:
            break

    print()
```

- `head is None`: 리스트가 비어 있는지 확인
- `current = head`: 첫 노드에서 순회 시작
- `current = current.link`: 다음 노드로 이동
- `current == head`: 처음 노드로 돌아왔는지 확인
- `break`: 반복문 종료

### 13. 노드 삽입과 삭제

삽입은 새 노드를 앞뒤 노드 사이에 연결하고, 삭제는 이전 노드가 삭제할 노드의 다음 노드를 가리키도록 수정한다.

#### 삽입 코드

```python
newNode.link = pre.link
pre.link = newNode
```

새 노드가 기존 다음 노드를 가리키게 한 다음, 이전 노드가 새 노드를 가리키도록 연결한다.

#### 삭제 코드

```python
pre.link = current.link
```

이전 노드가 삭제할 노드를 건너뛰고 다음 노드로 연결되게 한다.

첫 번째 노드나 마지막 노드를 삽입·삭제할 때는 `head`와 마지막 노드의 연결도 함께 확인해야 한다.

### 핵심 정리

- 원형 연결 리스트는 마지막 노드가 첫 번째 노드를 가리킨다.
- 노드는 `data`와 `link`로 구성된다.
- `head`는 첫 번째 노드를 가리킨다.
- 삽입과 삭제는 데이터 이동이 아니라 링크 변경으로 처리한다.
- 원형 구조는 처음 노드로 돌아왔는지 확인해 반복을 종료한다.
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