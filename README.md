# 소설처럼 읽는 장고 웹 프레임워크 - 실습 코드

[위키독스 교재](https://wikidocs.net/book/16995)의 실습 코드 저장소입니다.

Django로 게시판 웹 서비스를 단계별로 구현합니다.

## 사용 방법

원하는 챕터의 브랜치를 체크아웃하면 해당 시점까지의 완성된 프로젝트를 받을 수 있습니다.

```bash
# 저장소 클론
git clone https://github.com/sung2ne/textbook-django-board.git
cd textbook-django-board

# 원하는 챕터로 이동
git checkout part03/chapter-06   # PART 03의 06장까지 완성된 코드
```

## 브랜치 목록

각 브랜치는 해당 챕터까지의 코드가 누적 적용되어 독립적으로 실행 가능합니다.

### PART 02. 장고 프로젝트 만들기

| 브랜치 | 내용 |
|--------|------|
| `part02/chapter-01` | 장고 프로젝트 기본 설정 |

### PART 03. 게시글 앱 만들기

| 브랜치 | 내용 |
|--------|------|
| `part03/chapter-01` | 설계하기 |
| `part03/chapter-02` | 게시글 앱 만들기 |
| `part03/chapter-03` | 프로젝트에 게시글 앱 추가하기 |
| `part03/chapter-04` | STATIC 파일 만들기 |
| `part03/chapter-05` | 템플릿 파일 만들기 |
| `part03/chapter-06` | 게시글 등록 만들기 |
| `part03/chapter-07` | 게시글 보기 만들기 |
| `part03/chapter-08` | 게시글 수정 만들기 |
| `part03/chapter-09` | 게시글 삭제 기능 만들기 |
| `part03/chapter-10` | 게시글 목록 만들기 |

### PART 04. 게시글 목록 기능 개선하기

| 브랜치 | 내용 |
|--------|------|
| `part04/chapter-01` | 게시글 목록 페이징 처리하기 |
| `part04/chapter-02` | 게시글 검색 처리하기 |

### PART 05. 게시글 등록 및 수정 기능 개선하기

| 브랜치 | 내용 |
|--------|------|
| `part05/chapter-01` | 게시글 비밀번호 암호화 처리하기 |
| `part05/chapter-02` | 파일 업로드 기능 만들기 |
| `part05/chapter-03` | jQuery 적용하기 |
| `part05/chapter-04` | jQuery Validation Plugin 적용하기 |
| `part05/chapter-05` | TinyMCE 적용하기 |

### PART 06. 인증 기능 만들기

| 브랜치 | 내용 |
|--------|------|
| `part06/chapter-01` | 설계하기 |
| `part06/chapter-02` | 장고 앱 만들기 |
| `part06/chapter-03` | 회원 가입 기능 만들기 |
| `part06/chapter-04` | 로그인 기능 만들기 |
| `part06/chapter-05` | 로그아웃 기능 만들기 |
| `part06/chapter-06` | 프로필 보기 기능 만들기 |
| `part06/chapter-07` | 프로필 수정 기능 만들기 |
| `part06/chapter-08` | 비밀번호 수정 기능 만들기 |
| `part06/chapter-09` | 아이디 찾기 기능 만들기 |
| `part06/chapter-10` | 비밀번호 초기화 기능 만들기 |
| `part06/chapter-11` | 회원 탈퇴 기능 만들기 |

### PART 07. 게시판에 인증 적용하기

| 브랜치 | 내용 |
|--------|------|
| `part07/chapter-01` | 게시글 모델 수정하기 |
| `part07/chapter-02` | 게시글 등록 수정하기 |
| `part07/chapter-03` | 게시글 보기 수정하기 |
| `part07/chapter-04` | 게시글 수정 수정하기 |
| `part07/chapter-05` | 게시글 삭제 수정하기 |
| `part07/chapter-06` | 게시글 목록 수정하기 |
| `part07/chapter-07` | 게시글 첨부파일 수정하기 |

### PART 08. 게시글 댓글 기능 만들기

| 브랜치 | 내용 |
|--------|------|
| `part08/chapter-01` | 설계하기 |
| `part08/chapter-02` | 댓글 앱 만들기 |
| `part08/chapter-03` | 댓글 등록 만들기 |
| `part08/chapter-04` | 댓글 보기 만들기 |
| `part08/chapter-05` | 댓글 수정 만들기 |
| `part08/chapter-06` | 댓글 삭제 만들기 |

### PART 09. 사용자 관리 기능 만들기

| 브랜치 | 내용 |
|--------|------|
| `part09/chapter-01` | 슈퍼 유저 기능 이용하기 |
| `part09/chapter-02` | 설계하기 |
| `part09/chapter-03` | 사용자 앱 만들기 |
| `part09/chapter-04` | 사용자 목록 만들기 |
| `part09/chapter-05` | 사용자 보기 만들기 |
| `part09/chapter-06` | 사용자 삭제 만들기 |

### PART 99. 기타 기능 만들기

| 브랜치 | 내용 |
|--------|------|
| `part99/chapter-01` | OpenAI 활용하기 |

## 기술 스택

- **언어**: Python 3.12+
- **웹 프레임워크**: Django 5.2 (LTS)
- **데이터베이스**: SQLite (개발), MySQL (선택)
- **파일 업로드**: Django Media Files
- **폼 유효성 검사**: jQuery Validation Plugin
- **에디터**: TinyMCE
- **프론트엔드**: jQuery, Bootstrap

## 실행 방법

```bash
# 가상환경 생성 및 활성화
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows

# 의존성 설치
pip install -r requirements.txt

# 마이그레이션
cd mysite
python manage.py migrate

# 서버 실행
python manage.py runserver

# 브라우저에서 접속
# http://127.0.0.1:8000
```

## 프로젝트 구조

```
mysite/
├── manage.py
├── mysite/                  # 프로젝트 설정 패키지
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── posts/                   # 게시글 앱 (PART 03~)
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── admin.py
├── accounts/                # 인증 앱 (PART 06~)
│   ├── views.py
│   ├── urls.py
│   └── forms.py
├── comments/                # 댓글 앱 (PART 08~)
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── users/                   # 사용자 관리 앱 (PART 09~)
│   ├── views.py
│   └── urls.py
├── templates/               # HTML 템플릿
│   ├── base.html
│   ├── posts/
│   ├── accounts/
│   └── users/
├── static/                  # 정적 파일
│   ├── css/style.css
│   └── js/script.js
└── media/                   # 업로드 파일 (PART 05~)
```

## 라이선스

이 저장소는 [소설처럼 읽는 장고 웹 프레임워크](https://wikidocs.net/book/16995) 교재의 실습 코드입니다.
