# 1. Node.js 20 알파인 버전(가벼운 버전) 사용
FROM node:20-alpine

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 패키지 파일 복사 및 설치
COPY package.json package-lock.json* ./
RUN npm install

# 4. 소스 코드 복사
COPY . .

# 5. 개발 서버 실행 (프로덕션 배포 때는 build 명령어로 바꿈)
CMD ["npm", "run", "dev"]