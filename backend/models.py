from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime

class ImageRecord(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    filename: str  # 저장된 파일명
    original_filename: str # 사용자가 올린 원래 파일명
    created_at: datetime = Field(default_factory=datetime.utcnow)