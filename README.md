# 신성오 202630112
## 9월 17일 (3주차)
###

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