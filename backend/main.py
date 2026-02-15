import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# 우리가 만든 모듈들 가져오기
from database import create_db_and_tables
from routers import image

# 1. 앱 수명주기 관리 (Lifespan)
# 서버가 켜질 때 딱 한 번 실행되는 함수입니다.
@asynccontextmanager
async def lifespan(app: FastAPI):
    # (1) 업로드 폴더가 없으면 에러 나니까 미리 생성
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
        print("📁 'uploads' folder created.")
    
    # (2) DB 테이블 생성 (database.db 파일이 없으면 자동 생성됨)
    create_db_and_tables()
    print("✅ Database & Tables ready.")
    
    yield # 여기서부터 앱이 실행됩니다.
    
    print("🛑 Server shutting down...")

# 앱 생성 (lifespan 적용)
app = FastAPI(lifespan=lifespan)

# 2. CORS 설정 (프론트엔드 접속 허용) - 가장 중요! ⭐
# localhost와 127.0.0.1 둘 다 허용해야 안전합니다.
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "*"  # 개발 중에는 편의상 모든 곳 허용 (배포 시에는 끄는 게 좋음)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 위에서 정의한 주소들 허용
    allow_credentials=True,
    allow_methods=["*"],    # GET, POST, PUT, DELETE 등 모든 방식 허용
    allow_headers=["*"],    # 모든 헤더 허용
)

# 3. 정적 파일 서빙 (이미지 보기 기능)
# http://localhost:8000/static/파일명.jpg 로 접근 가능하게 함
app.mount("/static", StaticFiles(directory="uploads"), name="static")

# 4. 라우터(기능) 등록
# /images 로 시작하는 URL은 image.py가 처리함
app.include_router(image.router)

# 5. 헬스 체크용 기본 경로
@app.get("/")
def read_root():
    return {"status": "OK", "message": "Backend is running smoothly!"}