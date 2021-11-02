# [Assignment 1] 에이모

## 💁‍♀️ Project Link
📎 배포 주소 |

## ⭐ Basic Requirements
- 원티드 지원 과제 내용 포함
    - 유저 회원가입, 로그인
    - 게시글 CRUD
- 게시글 카테고리
- 게시글 검색
- 대댓글 (1 depth)
    - 대댓글 pagination
- 게시글 읽힘 수 
    - 같은 User가 게시글을 읽는 경우 count 수 증가하면 안 됨
- Rest API 설계
- Unit Test
- 1000만건 이상의 데이터를 넣고 성능테스트 진행 결과 필요

## 🛠 Built With
<img alt="Python" src ="https://img.shields.io/badge/Python-3776AB.svg?&style=for-the-badge&logo=Python&logoColor=white"/>
<img alt="Django" src ="https://img.shields.io/badge/Django-092E20.svg?&style=for-the-badge&logo=Django&logoColor=white"/>

## 🤔 구현한 방법과 이유에 대한 간략한 내용

### 사용자

- 사용자 생성 시 정규 표현식과 패스워드 확인으로 오류를 한 번 더 잡았습니다.
- 사용자 인증과 인가를 위한 로그인 시 jwt 토큰을 발행하고 사용합니다.
- jwt 토큰에 담고 있는 정보는 토큰 값과 user의 pk입니다.

### 게시물

- 게시물은 익명의 사용자가 생성, 삭제, 수정을 막기 위해 로그인을 해야 실행할 수 있습니다.
- 게시물 확인은 로그인을 하지 않아도 모두 불러올 수 있게끔 만들었습니다.
- 게시물을 작성한 사용자는 자신이 작성한 게시물을 확인하는 방법으로 로그인이 되었을 때 발급되는 jwt 토큰을 활용해 토큰의 id 값과 user의 pk를 비교하여 게시물을 작성한 본인만이 게시물을 수정 또는 삭제할 수 있습니다.
- 게시물은 조회할 때마다 counting 필드가 1씩 증가하도록 구현했습니다.
  - 같은 user가 같은 글을 읽는 경우 조회수가 올라가는 일을 막기 위해 유저의 ip 주소를 db에 저장하여 ip 주소와 post_id가 db에 저장되있는것과 일치한다면 조회수가 올라가지 않도록 구현했습니다.

### 댓글

- 댓글은 익명의 사용자가 생성, 삭제, 수정을 막기 위해 로그인을 해야 실행할 수 있습니다.
- 댓글 확인은 로그인을 하지 않아도 모두 불러올 수 있게끔 만들었습니다.
- comment 테이블의 nested_comment 필드가 NULL 값이라면 메인 댓글, comment_id를 가지고 있다면 대댓글입니다.
- 대댓글에는 대댓글을 달 수 없습니다. (nested_comment가 null이 아닐 시 대댓글 달 수 없음)

---

## 자세한 실행 방법(endpoint 호출방법)

### 구현 방법

- 가상환경 생성(conda사용을 가정) conda create -n (가상환경 이름)
- conda activate (생성한 가상환경 이름) 가상환경 실행
- git clone https://github.com/shinwooju/Wanted.git
- pip install -r requirements.txt를 입력하여 package install 진행
- python manage.py runserver 입력
- endpoint 호출 및 실행

### ENDPOINT

| Method | EndpointURL                | Request Body                          | Remark           |
| :----: | -------------------------- | ------------------------------------- | ---------------- |
|  POST  | /users/sign-up             | name, email, password, check_password | 회원가입         |
|  POST  | /users/sign-in             | email, password                       | 로그인           |
|  POST  | /posts                     | title, content                        | 게시물 작성      |
|  GET   | /posts/id                  |                                       | 게시물 조회      |
| DELETE | /posts/id                  |                                       | 게시물 삭제      |
|  PUT   | /posts/id                  | title, content                        | 게시물 수정      |
|  GET   | /posts/list?offset=&limit= |                                       | 게시물 목록 조회 |

---