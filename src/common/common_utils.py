import os

from dotenv import dotenv_values

from src.common.log_utils import log


@log
def check_and_load_env(env: str):
    """
    Check if environment file exists and load environment variables.

    Args:
        env: Environment name (e.g., 'int', 'prod')

    Returns:
        dict: Environment variables

    Raises:
        FileNotFoundError: If environment directory or file doesn't exist
    """
    env_dir = ".env"
    env_file = f"{env}.env"
    env_path = os.path.join(env_dir, env_file)

    # Check if .env directory exists
    if not os.path.exists(env_dir):
        raise FileNotFoundError(
            f"Environment directory '{env_dir}' does not exist. Please create it and add environment files."
        )

    # Get all .env files in the directory
    available_env_files = [f for f in os.listdir(env_dir) if f.endswith(".env")]

    # If no .env files exist at all
    if not available_env_files:
        raise FileNotFoundError(
            f"No environment files found in '{env_dir}' directory. Please create at least one .env file."
        )

    # Check if the specific env file exists
    if not os.path.exists(env_path):
        available_envs = [f.replace(".env", "") for f in available_env_files]
        raise FileNotFoundError(
            f"Environment file '{env_file}' not found in '{env_dir}' directory. "
            f"Available environments: {available_envs}"
        )

    env_vars = dotenv_values(dotenv_path=f".env/{env}.env")
    return env_vars
