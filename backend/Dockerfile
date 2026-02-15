# 1. 파이썬 3.9 슬림 버전(가벼운 버전)을 베이스로 사용
FROM python:3.9-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 의존성 파일 복사 및 설치 (캐시 효율을 위해 먼저 수행)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 소스 코드 복사
COPY . .

# 5. 실행 명령어 (중요: host를 0.0.0.0으로 설정해야 외부에서 접속 가능)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]