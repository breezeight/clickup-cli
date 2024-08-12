import httpx
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

CLICKUP_TOKEN = os.getenv("CLICKUP_PERSONAL_TOKEN")
API_URL = "https://api.clickup.com/api/v2"

def get_headers():
    return {
        "Authorization": CLICKUP_TOKEN,
        "Content-Type": "application/json"
    }

async def fetch_spaces(client: httpx.AsyncClient):
    response = await client.get(f"{API_URL}/space", headers=get_headers())
    response.raise_for_status()
    return response.json()

async def fetch_tasks(client: httpx.AsyncClient, space_id: str):
    response = await client.get(f"{API_URL}/space/{space_id}/task", headers=get_headers())
    response.raise_for_status()
    return response.json()