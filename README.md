# 신성오 202630112
## 10월 29일

## 10월 29일

### 1. 스택(Stack)의 개념

스택은 데이터를 차곡차곡 쌓는 자료구조이다.
**LIFO(Last In, First Out)** 구조로, 마지막에 넣은 데이터가 가장 먼저 나온다.

- `Push`: 데이터를 스택에 추가
- `Pop`: 스택의 가장 위에 있는 데이터 삭제
- `Peek`: 가장 위에 있는 데이터 확인
- `top`: 스택의 가장 위에 있는 데이터 위치

### 2. 스택 초기화 함수

스택의 크기를 지정하고 데이터를 저장할 공간을 만든다.
`top`을 `-1`로 설정하여 스택이 비어 있음을 나타낸다.

```python
def init_stack(size):
    global stack, top
    stack = [None] * size
    top = -1
```

- `global stack, top`: 함수 밖의 변수를 사용
- `[None] * size`: 지정한 크기만큼 스택 생성
- `top = -1`: 스택이 비어 있는 상태

### 3. Push 함수

스택에 새로운 데이터를 추가한다.
스택이 가득 찼는지 확인한 뒤 `top`을 증가시키고 데이터를 저장한다.

```python
def push(data):
    global top
    if is_stack_full():
        return print("스택이 가득 찼습니다")
    else:
        top += 1
        stack[top] = data
        return print("Push된 데이터: " + str(data) + ", 현재 top: " + str(top))
```

- `is_stack_full()`: 스택이 가득 찼는지 확인
- `top += 1`: 데이터가 들어갈 위치로 이동
- `stack[top] = data`: 해당 위치에 데이터 저장

### 4. Pop 함수

스택의 가장 위에 있는 데이터를 삭제한다.
데이터를 변수에 저장하고 해당 위치를 비운 뒤 `top`을 감소시킨다.

```python
def pop():
    global top
    if is_stack_empty():
        return print("스택이 비어 있습니다")
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        return print("Pop된 데이터: " + str(data) + ", 현재 top: " + str(top))
```

- `is_stack_empty()`: 스택이 비어 있는지 확인
- `data = stack[top]`: 가장 위의 데이터 저장
- `stack[top] = None`: 해당 위치 비우기
- `top -= 1`: 이전 위치로 이동

### 5. 스택 가득 참 확인 함수

`top`이 스택의 마지막 인덱스와 같으면 스택이 가득 찬 상태이다.

```python
def is_stack_full():
    global top
    if top == len(stack) - 1:
        return True
    else:
        return False
```

- `len(stack)`: 스택의 전체 크기
- `len(stack) - 1`: 마지막 인덱스
- `return True`: 스택이 가득 찬 상태
- `return False`: 아직 공간이 남은 상태

### 6. 스택 비어 있음 확인 함수

`top`이 `-1`이면 스택에 데이터가 없는 상태이다.

```python
def is_stack_empty():
    global top
    if top == -1:
        return True
    else:
        return False
```

- `top == -1`: 스택이 비어 있는지 확인
- `return True`: 비어 있음
- `return False`: 데이터가 있음

### 7. Peek 함수

스택에서 데이터를 삭제하지 않고 가장 위에 있는 데이터를 확인한다.

```python
def peek():
    global top
    if is_stack_empty():
        return print("스택이 비어 있습니다. peek 불가")
    else:
        data = stack[top]
        return print("Peek된 데이터: " + str(data) + ", 현재 top: " + str(top))
```

- `data = stack[top]`: 가장 위에 있는 데이터 확인
- `Pop`과 달리 `top`을 변경하거나 데이터를 삭제하지 않는다.
- 스택이 비어 있으면 데이터를 확인할 수 없다.

### 8. 스택 상태 출력 함수

스택의 데이터를 위에서 아래 방향으로 출력한다.
`range()`의 시작값과 증가 방향을 조절해 마지막 인덱스부터 반복한다.

```python
def print_stack():
    print("=== 스택 상태 ===")
    for i in range(len(stack) - 1, -1, -1):
        print(stack[i])
    print("=================")
```

- `len(stack) - 1`: 마지막 인덱스부터 시작
- `-1`: 반복이 끝나는 기준값으로, 실제 반복에는 포함되지 않음
- `-1`의 간격: 인덱스를 1씩 감소
- `stack[i]`: 해당 위치의 데이터 출력

### 9. 스택 초기화하기

`init_stack()` 함수를 호출해 스택의 크기를 지정한다.

```python
init_stack(7)

print_stack()
```

- `init_stack(7)`: 크기가 7인 스택 생성
- `print_stack()`: 현재 스택 상태 확인

### 10. 데이터 Push 하기

`push()` 함수를 이용해 스택에 데이터를 차례대로 추가한다.
스택의 크기를 초과해 데이터를 추가하면 가득 찼다는 메시지를 표시한다.

```python
push("커피")
push("녹차")
push("꿀물")
push("레몬차")
push("밀크티")
push("오렌지주스")
push("아이스티")

push("콜라")

print_stack()
```

- 데이터를 추가할 때마다 `top`이 1씩 증가한다.
- 스택의 크기가 7이면 최대 7개의 데이터를 저장할 수 있다.
- 가득 찬 상태에서 추가하면 `Push`가 실행되지 않는다.

### 11. 데이터 Pop 하기

`pop()` 함수를 호출해 가장 위에 있는 데이터를 차례대로 삭제한다.
스택이 비어 있으면 더 이상 데이터를 삭제할 수 없다.

```python
pop()
pop()
pop()
pop()
pop()
pop()
pop()

pop()

peek()

print_stack()
```

- `pop()`: 가장 위에 있는 데이터 삭제
- 스택이 비어 있을 때 `pop()`을 호출하면 삭제하지 않는다.
- `peek()`: 데이터 삭제 없이 가장 위의 데이터 확인
- `print_stack()`: 현재 스택 상태 출력

### 핵심 정리

- 스택은 LIFO 구조로, 마지막에 들어온 데이터가 먼저 나간다.
- `Push`는 데이터를 추가하고 `Pop`은 데이터를 삭제한다.
- `Peek`는 데이터를 삭제하지 않고 확인한다.
- `top = -1`이면 스택이 비어 있다.
- `top == len(stack) - 1`이면 스택이 가득 찬 상태이다.
- 스택의 크기를 초과하거나 비어 있는 상태에서 작업하지 않도록 확인 함수가 필요하다.


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