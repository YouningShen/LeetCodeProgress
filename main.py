# main.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import asyncio

from leetcode import fetch_user_stats
from dashboard import create_bar_chart

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# List your group members' LeetCode usernames
usernames = ["user1", "user2", "user3"]

@app.get("/", response_class=HTMLResponse)
async def read_dashboard(request: Request):
    tasks = [fetch_user_stats(username) for username in usernames]
    user_stats = await asyncio.gather(*tasks)
    chart_html = create_bar_chart(user_stats)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "chart_html": chart_html
    })
