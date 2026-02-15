from sqlmodel import SQLModel, create_engine, Session

# 도커 내부에서는 파일이 생성될 경로가 중요합니다.
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# check_same_thread는 SQLite 전용 설정
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session