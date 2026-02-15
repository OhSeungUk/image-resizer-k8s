# backend/services/processing.py
import os
import uuid
from PIL import Image

UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

def process_image(file_obj, filename: str) -> str:
    """
    이미지를 받아서 처리 후 저장하고, 파일 경로를 반환하는 함수
    """
    # 1. 고유 파일명 생성
    unique_filename = f"{uuid.uuid4()}_{filename}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    # 2. 이미지 처리
    try:
        image = Image.open(file_obj)
        image = image.convert("L") # 흑백 변환
        image.thumbnail((300, 300)) # 리사이징
        image.save(file_path)
        return unique_filename
    except Exception as e:
        raise e