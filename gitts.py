#!/usr/bin/env python3
import argparse
import os
import subprocess
import sys
from datetime import datetime, timedelta
from typing import Dict, List


def parse_arguments() -> argparse.Namespace:
    """
    Parse and set up command line arguments.

    Returns:
        argparse.Namespace: Parsed command line arguments with attributes 'offset_minutes' and 'git_command'.
    """
    parser = argparse.ArgumentParser(
        description="Run git commands with a time offset for the commit timestamp."
    )
    parser.add_argument(
        "offset_minutes", type=int, help="Time offset in minutes, can be negative."
    )
    parser.add_argument(
        "git_command",
        nargs=argparse.REMAINDER,
        help="Git command followed by any arguments.",
    )
    return parser.parse_args()


def calculate_future_time(offset_minutes: int) -> str:
    """
    Shift the current time by the specified number of minutes and return it as an ISO 8601 formatted string.

    Args:
        offset_minutes (int): The number of minutes to offset the current time by, can be negative.

    Returns:
        str: The future time formatted as an ISO 8601 string.

    Raises:
        ValueError: If the offset_minutes value is invalid.
    """
    try:
        future_time: datetime = datetime.now() + timedelta(minutes=offset_minutes)
        return future_time.strftime("%Y-%m-%dT%H:%M:%S")
    except ValueError as e:
        raise ValueError(f"Invalid offset_minutes value: {offset_minutes}. Error: {e}")


def set_environment_variables(formatted_time: str) -> Dict[str, str]:
    """
    Set up Git environmental variables for author and committer dates and return the environment dictionary.

    Args:
        formatted_time (str): The date and time in ISO 8601 format to be used for GIT_AUTHOR_DATE and GIT_COMMITTER_DATE.

    Returns:
        Dict[str, str]: A dictionary containing the modified environment variables.
                        The keys are the environment variable names (e.g., 'GIT_AUTHOR_DATE', 'GIT_COMMITTER_DATE'),
                        and the values are the corresponding formatted_time string.
    """
    env: Dict[str, str] = {
        **os.environ,
        "GIT_AUTHOR_DATE": formatted_time,
        "GIT_COMMITTER_DATE": formatted_time,
    }
    return env


def run_git_command(git_command: List[str], env: Dict[str, str]) -> None:
    """
    Execute a Git command using the specified environment variables.

    Args:
        git_command (List[str]): The Git command and its arguments to execute.
        env (Dict[str, str]): The environment variables to use during the execution.

    Raises:
        subprocess.CalledProcessError: If the Git command fails.
    """
    subprocess.run(["git"] + git_command, env=env, check=True)


def main() -> None:
    """
    Main function to orchestrate parsing arguments, calculating future time, setting environment variables, and running the Git command.
    """
    try:
        args = parse_arguments()
        formatted_time = calculate_future_time(args.offset_minutes)
        env = set_environment_variables(formatted_time)
        run_git_command(args.git_command, env)
    except ValueError as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(
            f"Git command 'git {' '.join(args.git_command)}' failed with error: {e}",
            file=sys.stderr,
        )
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
