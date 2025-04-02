from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import base64

USERNAME = "admin"
PASSWORD = "secret"

app = FastAPI()

# CORS 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def check_basic_auth(request: Request):
    auth = request.headers.get("Authorization")
    if not auth or not auth.startswith("Basic "):
        raise HTTPException(status_code=401, detail="Unauthorized")
    encoded = auth.split(" ")[1]
    decoded = base64.b64decode(encoded).decode()
    user, pwd = decoded.split(":")
    if user != USERNAME or pwd != PASSWORD:
        raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/transcript")
async def get_transcript(video_id: str, request: Request):
    check_basic_auth(request)
    return {"transcript": f"Mock transcript for video_id: {video_id}"}
