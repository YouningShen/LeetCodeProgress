# leetcode.py
import aiohttp
from bs4 import BeautifulSoup

async def fetch_user_stats(username: str):
    url = f"https://leetcode.com/{username}/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            html = await resp.text()
            soup = BeautifulSoup(html, 'html.parser')

            # Look for stats
            script_tags = soup.find_all("script")
            for script in script_tags:
                if "submissionCalendar" in script.text:
                    text = script.text
                    break

            # Simple fallback (for total solved)
            total_solved_tag = soup.find("span", string="Solved")
            if total_solved_tag:
                solved = total_solved_tag.find_previous("span").text
                return {"username": username, "total_solved": solved}
            return {"username": username, "error": "Could not parse data"}
