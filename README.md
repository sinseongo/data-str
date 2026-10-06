# 신성오 202630112

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