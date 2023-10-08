import os
import subprocess
import uuid
import re  # Import the re module for URL validation
import logging
import sys

sys.path.append(".")
from app.src.config import config

# Configure logging using the settings from the JSON file
# logging.basicConfig(
#     level=getattr(logging, config["logging"]["level"]),
#     format=config["logging"]["format"],
#     filename=config["logging"]["file"],
#     filemode=config["logging"]["file_mode"],
# )


def init_project():
    # Get the project name from the user
    project_name = input("Enter the project name: ")

    # Generate a unique identifier
    unique_id = str(uuid.uuid4())[:8]
    print(f"unique_id: {unique_id}")
    logging.info(f"unique_id: {unique_id}")

    # Combine the project name and unique identifier
    project_name_with_id = f"{project_name}_{unique_id}"

    base_dir = os.path.expanduser(config["base_dir"])
    # Create a new directory for the project
    project_dir = os.path.join(
        base_dir,
        project_name_with_id,
    )
    logging.info(f"project_dir: {project_dir}")
    os.makedirs(project_dir)
    os.makedirs(os.path.join(project_dir, "tasks"))
    os.makedirs(os.path.join(project_dir, "attachments"))
    logging.info("made dirs")

    # Create a project.md file for project-specific information
    with open(os.path.join(project_dir, "project.md"), "w") as project_file:
        project_file.write("running ticket number: 0\n\n")
        project_file.write(f"# {project_name}\n\n")
        project_file.write("Project description and details go here.\n")

    # Initialize a Git repository in the project directory
    subprocess.run(["git", "init"], cwd=project_dir, check=True)

    # Ask the user for a remote Git repository URL
    remote_url = input(
        "Enter a remote Git repository URL (or press Enter to skip): "
    ).strip()

    # Validate the remote URL using a basic regex pattern
    while (
        remote_url
        and not re.match(r"^(https?|git)://", remote_url)
        and not re.match(r"^(git@)", remote_url)
    ):
        print(
            "Invalid remote URL. Please use a valid HTTP, HTTPS, or Git URL or leave blank."
        )
        remote_url = input(
            "Enter a remote Git repository URL (or press Enter to skip): "
        ).strip()
    if remote_url:
        # Add the remote repository if a valid URL is provided
        print("Adding remote repository...")
        subprocess.run(
            ["git", "remote", "add", "origin", remote_url], cwd=project_dir, check=True
        )

    print(f"Project '{project_name_with_id}' created successfully!")


if __name__ == "__main__":
    init_project()
