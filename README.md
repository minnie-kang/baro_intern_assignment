# baro_intern_assignment

### 네비게이션 
1. [개요](#프로젝트-개요)
2. [기술 스택](#기술-스택)
3. [프로젝트 요구사항](#프로젝트-요구사항)
4. [개발 환경 세팅](#개발-환경-세팅)


&nbsp;
&nbsp;

## 🌼 프로젝트 개요

- **과제**: **Django**를 이용하여 JWT 인증/인가 로직을 구현하고, **Pytest** 기반 테스트 코드 작성 후 AWS EC2에 배포까지 진행합니다.
- **제출 방법**: 과제 요구사항에 맞춰 코드를 작성한 뒤, **Public** 리포지토리를 생성하고 링크를 제출하세요.
- 기본으로 설정된 서버의 주소와 포트는 `0.0.0.0:8000` 이고, 이를 수정하지 않는다.
- 모든 API 응답은 적절한 상태 코드와 `application/json` 형식으로 반환한다.



&nbsp;
&nbsp;

## ⚙️ 기술 스택

#### Backend: <img src="https://img.shields.io/badge/Python%203.12-3776AB?style=for-the-badge&logo=python&logoColor=white">  <img src="https://img.shields.io/badge/django 5.2.1-092E20?style=for-the-badge&logo=django&logoColor=white"> <img src="https://img.shields.io/badge/django rest framework-092E20?style=for-the-badge&logo=django&logoColor=white"> <img src="https://img.shields.io/badge/AMAZON EC2-FFE900?style=for-the-badge&logo=amazon&logoColor=black">

#### Database: <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"><img src="https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white">

&nbsp;
&nbsp;


## 📋 프로젝트 요구사항

### 사용자 회원가입

#### Request Body 예시
```
{
  "username": "JIN HO",
  "password": "12341234",
  "nickname": "Mentos"
}
```
![Image](https://github.com/user-attachments/assets/fed051f1-c1d1-4702-a5b1-9d540506d8d6)

#### Response Body 예시
```

// 회원가입에 성공한 경우
{
  "username": "JIN HO",
  "nickname": "Mentos",
}


// 회원가입에 실패한 경우
{
  "error": {
    "code": "USER_ALREADY_EXISTS",
    "message": "이미 가입된 사용자입니다."
  }
}
```
![Image](https://github.com/user-attachments/assets/ff35b0bb-360d-41dc-b700-1bfd7b885b40)

### 사용자 로그인(API)
#### Request Body 예시
```
{
  "username": "JIN HO",
  "password": "12341234"
}
```

#### Response Body 예시(상황 추가)
```
// 로그인에 성공한 경우
{
  "token": "eKDIkdfjoakIdkfjpekdkcjdkoIOdjOKJDFOlLDKFJKL"
}

// 로그인에 실패한 경우
{
  "error": {
    "code": "INVALID_CREDENTIALS",
    "message": "아이디 또는 비밀번호가 올바르지 않습니다."
  }
}
```

![Image](https://github.com/user-attachments/assets/60cd61bd-493e-41b2-a8f9-35c575c7dfa8)


![Image](https://github.com/user-attachments/assets/dbfc4a75-a4c1-4c3e-bb63-2194ec30c4f9)

### AUTH
#### Response 예시
```
// 만료된 토큰인 경우
{
  "error": {
    "code": "TOKEN_EXPIRED",
    "message": "토큰이 만료되었습니다."
  }
}
```
![Image](https://github.com/user-attachments/assets/ff0371ae-140c-4c27-8ad8-ca49a6dc92e5)

```
// 토큰이 없는 경우
{
  "error": {
    "code": "TOKEN_NOT_FOUND",
    "message": "토큰이 없습니다."
  }
}
```
![Image](https://github.com/user-attachments/assets/17833be3-e618-4abb-b90c-eec543d79234)
```
// 유효하지 않은 토큰인 경우
{
  "error": {
    "code": "INVALID_TOKEN",
    "message": "토큰이 유효하지 않습니다."
  }
}
```
![Image](https://github.com/user-attachments/assets/d284c47a-7776-4287-b415-aceec53a9e8d)

---------------------------------------

### pytest테스트
- **목적:**
각 기능(회원가입, 로그인 등)이 의도한 대로 동작하는지 확인합니다.
- **구현 포인트:**
    - 각 API 엔드포인트 별 올바른 입력과 잘못된 입력에 대해 테스트 케이스를 작성합니다.
    - 예를 들어, 회원가입의 경우 정상적인 사용자 정보와 이미 가입된 사용자 정보에 대해 테스트합니다.
    - 로그인의 경우 올바른 자격 증명과 잘못된 자격 증명을 테스트하여, 성공/실패 시의 응답 구조가 예상과 동일한지 확인합니다.
![Image](https://github.com/user-attachments/assets/db80554d-6532-4b7d-b6cb-d8c3b7bef478)

![Image](https://github.com/user-attachments/assets/4681a5f9-88c3-4207-918f-bc786bbb9c11)

![Image](https://github.com/user-attachments/assets/424dbb66-4f20-45d5-8108-425404f15b4f)

---------------------------------------

### API 명세서
**Swagger를 사용한 API 문서화**

- **목적:**
각 엔드포인트, 요청/응답 구조, 상태 코드 등을 한눈에 파악할 수 있도록 문서화합니다.
- **구현 포인트:**
    - Swagger (또는 OpenAPI) 스펙을 기반으로 API 문서화 도구를 프로젝트에 추가합니다.
    - 각 API에 대한 설명, 파라미터, 요청/응답 예시 등을 Swagger UI에 등록하여, 브라우저에서 쉽게 확인할 수 있도록 합니다.
    - `/swagger` 로 접근하여 문서를 확인할 수 있도록 구성합니다.

http://15.164.48.165:8000/swagger/
![APIImage](https://github.com/user-attachments/assets/50f83d43-4400-45d2-bf13-3f73411a43a5)

---------------------------------------

### 배포 (Python  버전)
**AWS EC2를 활용한 서버 배포 (**Python**)**

- **목적:**
    
    개발한 Python 애플리케이션을 실제 운영 환경에서 동작하도록 EC2 인스턴스에 배포합니다.
    
- **구현 포인트:**
    - **EC2 인스턴스 생성:**
        
        AWS 콘솔을 통해 적절한 사양의 인스턴스를 생성하고 백그라운드에서 안정적으로 실행되는 서버를 배포합니다.


&nbsp;
&nbsp;


## 💻 개발 환경 세팅
#### 1. 가상환경 생성
```
맥
python3 -m venv venv

윈도우
python -m venv venv
```


#### 2. 가상환경 활성화   
```
맥
source venv/Scripts/activate

윈도우
venv/Scripts/activate
```


#### 3. 패키지 설치
```
pip install -r requirements.txt
```


#### 4. 데이터 베이스 도커 실행
```
docker-compose build
docker-compose up
```


#### 5. 마이그레이션 및 마이그레이트
```
python manage.py makemigrations
python manage.py migrate
```