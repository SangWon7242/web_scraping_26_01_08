# Web Scrap 가상환경

웹 스크래핑 프로젝트를 위한 Python 가상환경입니다.

## 📁 프로젝트 구조

```
python_projects/
├── web_scrap/          # Python 가상환경
│   ├── Include/        # C 헤더 파일 (확장 빌드용)
│   ├── Lib/            # 설치된 패키지 저장소
│   ├── Scripts/        # 실행 스크립트 (activate, python, pip)
│   └── pyvenv.cfg      # 가상환경 설정 파일
└── README.md           # 프로젝트 문서
```

## 🚀 시작하기

### 가상환경 활성화

**Windows CMD:**
```bash
web_scrap\Scripts\activate
```

**Windows PowerShell:**
```powershell
web_scrap\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
source web_scrap/bin/activate
```

### 가상환경 비활성화

```bash
deactivate
```

## 📦 추천 패키지

웹 스크래핑에 유용한 패키지들:

```bash
# HTTP 요청
pip install requests

# HTML 파싱
pip install beautifulsoup4 lxml

# 동적 웹페이지 (JavaScript 렌더링)
pip install selenium

# 비동기 스크래핑
pip install aiohttp

# 고급 스크래핑 프레임워크
pip install scrapy
```

## 📋 패키지 관리

### 설치된 패키지 확인
```bash
pip list
```

### 패키지 목록 저장
```bash
pip freeze > requirements.txt
```

### 패키지 일괄 설치
```bash
pip install -r requirements.txt
```

## 📅 생성일

- **생성일**: 2026-01-08
- **Python 버전**: 3.x
