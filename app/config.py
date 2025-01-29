import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    EMAIL = os.getenv("EMAIL", "zalmat.online.courses@example.com")
    GITHUB_URL = os.getenv("GITHUB_URL", "https://github.com/imadoszmt/Hng12_Backend_Stage0_API-Project")