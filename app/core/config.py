import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

class Settings:
    PROJECT_NAME: str = "Ai Shorts Project"
    CONNECTION_STRING: str = os.getenv("CONNECTION_STRING")

settings = Settings() 