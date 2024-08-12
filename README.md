
# Setup your env


# Run Your CLI Tool

You can run your CLI commands with Poetry. First, make sure your environment is set up:  poetry install

Then you can run your CLI commands:

```bash
poetry run python clickup_cli/main.py spaces list --team-id YOUR_team_id_PARAMETER

poetry run python clickup_cli/main.py tasks list --space-id YOUR_SPACE_ID
```


# Architecture

## CLI with Typer

We’ve used [Typer](https://typer.tiangolo.com/) to build a command-line interface (CLI) for interacting with ClickUp's API. Typer makes it easy to create and manage CLI applications with Python, providing powerful features like automatic help generation and type checking.

### Overview

Our CLI application is organized using subcommands to provide a clear and structured way to interact with the ClickUp API. Currently, it includes the following commands:

- **`spaces list`**: Lists spaces for a specified team.

### Example Usage

To list spaces for a specific team, use the following command:

```sh
python clickup_cli/main.py spaces list --team-id YOUR_team_id_PARAMETER
```

Replace `YOUR_team_id_PARAMETER` with the ID of the team you want to query. This command will fetch and display the list of spaces associated with the specified team.

### Expanding the CLI

The CLI is designed to be easily extendable. Here’s how you can add new functionality:

1. **Add New Subcommands**: To introduce new commands like `tasks` or `projects`, create a new module for each set of related commands. For example, to add a `tasks` command, create a file named `tasks.py` in the `clickup_cli` directory.

   ```python
   # clickup_cli/tasks.py
   import typer
   from clickup_cli.client import fetch_tasks  # Assume you define fetch_tasks in client.py
   import asyncio

   app = typer.Typer()

   @app.command(name="list")
   def list_tasks(
       team_id: str = typer.Option(..., help="The ID of the team to list tasks for.")
   ):
       """
       List tasks for a specific team.

       Args:
           team_id (str): The ID of the team to list tasks for.
       """
       try:
           tasks_data = asyncio.run(fetch_tasks(team_id))
           print(tasks_data)
       except Exception as e:
           print(f"An error occurred: {e}")
   ```

2. **Integrate Subcommands**: Update `main.py` to include the new subcommands:

   ```python
   # clickup_cli/main.py
   import typer
   from clickup_cli.spaces import app as spaces_app
   from clickup_cli.tasks import app as tasks_app

   app = typer.Typer()

   # Add the spaces and tasks subcommands to the main app
   app.add_typer(spaces_app, name="spaces")
   app.add_typer(tasks_app, name="tasks")

   if __name__ == "__main__":
       app()
   ```

3. **Typer Philosophy**: Typer allows you to create complex CLI applications in a straightforward way. Each `Typer` instance represents a set of related commands. You can nest commands and options to create a hierarchical CLI structure. Commands are defined as functions with parameters, and Typer automatically handles parsing and validation.

### Code Structure

- **`clickup_cli/settings.py`**: Manages configuration and environment variables.
- **`clickup_cli/client.py`**: Contains functions for making API requests.
- **`clickup_cli/spaces.py`**: Defines commands related to spaces.
- **`clickup_cli/tasks.py`**: (Example) Defines commands related to tasks.
- **`clickup_cli/main.py`**: Integrates subcommands into the main CLI application.

Feel free to explore and extend the CLI to fit your needs!

---

This updated `README.md` provides a clear example of using the `spaces list` command, instructions for expanding the CLI with additional subcommands, and an overview of the Typer philosophy to guide future development.