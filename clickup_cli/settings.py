from pydantic_settings import BaseSettings
from pydantic import Field, ValidationError
from dotenv import load_dotenv
import typer

# Load environment variables from a .env file
# This allows us to use environment variables defined in the .env file
load_dotenv()


# import os
# # Print all environment variables for debugging
# print("Environment Variables:")
# for key, value in os.environ.items():
#     print(f"{key}={value}")

class Settings(BaseSettings):
    # Define a required setting for ClickUp personal token
    # The token must be provided via an environment variable
    # In Pydantic, setting a field to be required is straightforward: you use the ... (ellipsis) in the Field definition, which indicates that the field must be provided and is mandatory.
    clickup_personal_token: str = Field(..., env="CLICKUP_PERSONAL_TOKEN")

    class Config:
        # Specify the path to the .env file
        # This tells pydantic to read the environment variables from this file
        env_file = ".env"
        # Define the encoding of the .env file
        # This ensures that pydantic reads the .env file using UTF-8 encoding
        env_file_encoding = 'utf-8'

# Try to Instantiate settings and handle validation
try:
    settings = Settings()
except ValidationError as e:
    typer.secho(f"Configuration Error: {e}", fg=typer.colors.RED, err=True)
    raise SystemExit(1)