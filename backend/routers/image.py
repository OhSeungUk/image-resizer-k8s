from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlmodel import Session, select
from typing import List

from services.processing import process_image
from database import get_session
from models import ImageRecord

router = APIRouter(prefix="/images", tags=["images"])

# 1. 업로드 및 DB 저장
@router.post("/upload")
async def upload_image_endpoint(
    file: UploadFile = File(...), 
    session: Session = Depends(get_session) # DB 세션 주입
):
    try:
        # 이미지 처리 (파일 저장)
        saved_filename = process_image(file.file, file.filename)
        
        # DB 저장 (INSERT)
        record = ImageRecord(
            filename=saved_filename, 
            original_filename=file.filename
        )
        session.add(record)
        session.commit()
        session.refresh(record) # ID 등 자동생성된 값 가져오기
        
        return {
            "message": "성공!",
            "url": f"http://localhost:8000/static/{saved_filename}",
            "id": record.id
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 2. 히스토리 조회 (새로 추가된 기능!)
@router.get("/history", response_model=List[ImageRecord])
async def get_history(session: Session = Depends(get_session)):
    # 최신순으로 정렬해서 가져오기
    statement = select(ImageRecord).order_by(ImageRecord.id.desc())
    results = session.exec(statement).all()
    return results