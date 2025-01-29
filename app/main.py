from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from app.config import Config
import pytz

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["GET"],  
    allow_headers=["*"],
)

@app.get("/")
async def get_info():
    # Get current UTC time and format to ISO 8601
    current_time = datetime.now(pytz.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
    
    return {
        "email": Config.EMAIL,
        "current_datetime": current_time,
        "github_url": Config.GITHUB_URL
    }