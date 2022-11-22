# clickPaybookPassword

페이북 비밀번호 결재를 위한 example입니다.

## 작동원리
 1. selenium에서 password 이미지를 저장한다.
 2. openCV의 image검색을 통해서 특정 숫자의 위치를 얻는다.
 3. 얻은 위치를 selenium의 actionChain을 통해서 수행한다.

## 설치
```
pip install -r requirements.txt
```

## 사용방법
 ```
 python test.py
 ```
