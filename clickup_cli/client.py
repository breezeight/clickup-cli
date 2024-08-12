import httpx
from typing import Dict, Any
from .settings import settings

async def create_client() -> httpx.AsyncClient:
    """
    Create and return an httpx.AsyncClient object with the appropriate headers.
    
    Returns:
        httpx.AsyncClient: A configured httpx.AsyncClient object.
    """
    client = httpx.AsyncClient()
    client.headers.update({
        "Authorization": settings.clickup_personal_token,
        "Content-Type": "application/json"
    })
    return client

async def fetch_spaces(team_id: str) -> Dict[str, Any]:
    """
    Fetch spaces for a specific team from the ClickUp API.
    
    Args:
        team_id (str): The ID of the team to fetch spaces for.
    
    Returns:
        Dict[str, Any]: The JSON response from the API as a dictionary.
    """
    client = await create_client()
    url = f"https://api.clickup.com/api/v2/team/{team_id}/space"
    query = {"archived": "false"}
    response = await client.get(url, params=query)
    await client.aclose()
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to retrieve data: {response.status_code} - {response.text}")