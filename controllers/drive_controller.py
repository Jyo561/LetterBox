from fastapi import FastAPI, Request, Depends, HTTPException, APIRouter
from fastapi.responses import RedirectResponse, JSONResponse
import httpx
import os
import io
import google.auth
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from dotenv import load_dotenv
from starlette.middleware.sessions import SessionMiddleware
from googleapiclient.http import MediaIoBaseUpload

router = APIRouter()

@router.post("/upload")
async def upload_to_drive(request: Request):
    token = request.session.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Unauthorized")

    body = await request.json()
    content = body["content"]
    filename = body.get("filename", "My Letter")

    creds = Credentials(token)
    drive_service = build("drive", "v3", credentials=creds)

    media = MediaIoBaseUpload(io.BytesIO(content.encode()), mimetype="text/plain")
    file_metadata = {"name": filename, "mimeType": "application/vnd.google-apps.document"}

    file = drive_service.files().create(body=file_metadata, media_body=media).execute()
    
    return JSONResponse(content={"fileId": file.get("id"), "message": "File uploaded successfully!"})
