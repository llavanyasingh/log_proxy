from fastapi import FastAPI, HTTPException
import httpx
import os

app = FastAPI()

NGROK_URL = os.getenv("NGROK_URL")  # Set this in Render's environment settings

@app.get("/logs")
async def proxy_logs():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{NGROK_URL}/logs", timeout=10)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Failed to fetch logs: {str(e)}")
