import typer
from clickup_cli.spaces import app as spaces_app

app = typer.Typer()

# Add the spaces subcommands to the main app
app.add_typer(spaces_app, name="spaces")

if __name__ == "__main__":
    app()