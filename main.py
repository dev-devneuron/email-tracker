from fastapi import FastAPI, Request
from fastapi.responses import Response, RedirectResponse

app = FastAPI()

# open tracking
@app.get("/open")
async def track_open(lead_id: str, request: Request):

    ip = request.client.host
    ua = request.headers.get("user-agent")

    print("OPEN EVENT")
    print("Lead:", lead_id)
    print("IP:", ip)
    print("User Agent:", ua)

    return Response(content=b"", media_type="image/png")


# click tracking
@app.get("/click")
async def track_click(lead_id: str, url: str, request: Request):

    ip = request.client.host
    ua = request.headers.get("user-agent")

    print("CLICK EVENT")
    print("Lead:", lead_id)
    print("IP:", ip)
    print("User Agent:", ua)

    return RedirectResponse(url)