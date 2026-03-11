import os
from fastapi import FastAPI, Request
from fastapi.responses import Response, RedirectResponse
from supabase import create_client

app = FastAPI()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


@app.get("/open")
async def track_open(lead_id: str, request: Request):
    ip = request.client.host
    ua = request.headers.get("user-agent")

    # insert into Supabase
    supabase.table("email_events").insert({
        "lead_id": lead_id,
        "event_type": "open",
        "ip_address": ip,
        "user_agent": ua
    }).execute()

    return Response(content=b"", media_type="image/png")


@app.get("/click")
async def track_click(lead_id: str, url: str, request: Request):
    ip = request.client.host
    ua = request.headers.get("user-agent")

    supabase.table("email_events").insert({
        "lead_id": lead_id,
        "event_type": "click",
        "ip_address": ip,
        "user_agent": ua
    }).execute()

    return RedirectResponse(url)