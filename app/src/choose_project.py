import os
import subprocess
import uuid
import re
import sys
import logging


sys.path.append(".")
from app.src.config import config

base_dir = config["base_dir"]
logging.info(f"base_dir: {base_dir}")
# the base dir might include ~ so we need to expand it
base_dir = os.path.expanduser(base_dir)


# Function to list available projects
def list_projects():
    if not os.path.exists(base_dir):
        logging.info(f"base_dir: {base_dir} does not exist")
        return []
    logging.info(f"os.listdir(base_dir): {os.listdir(base_dir)}")
    return [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]


def choose_project():
    projects = list_projects()
    if not projects:
        print("No projects found. Please create a project first.")
        return None

    # Run fzf to interactively select a project
    selected_project = subprocess.run(
        ["fzf"], input="\n".join(projects), text=True, stdout=subprocess.PIPE
    )

    if selected_project.returncode == 0:
        return selected_project.stdout.strip()
    else:
        print("No project selected.")
        return None
