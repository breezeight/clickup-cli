import typer
from clickup_cli.client import fetch_spaces
import asyncio

app = typer.Typer()

@app.command(name="list")
def list_spaces(
    team_id: str = typer.Option(..., help="The ID of the team to list spaces for.")
):
    """
    List spaces for a specific team.
    
    Args:
        team_id (str): The ID of the team to list spaces for (Workspace). Find it from the url: "https://app.clickup.com/1234567/..."  in this case 1234567 is the workspace/team .

.
    """
    try:
        spaces_data = asyncio.run(fetch_spaces(team_id))
        print(spaces_data)
    except Exception as e:
        print(f"An error occurred: {e}")