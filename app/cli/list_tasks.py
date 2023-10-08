import os
import subprocess
import uuid
import re
import sys
import logging

sys.path.append(".")
from app.src.config import config
from app.src.choose_project import choose_project

base_dir = config["base_dir"]
logging.info(f"base_dir: {base_dir}")
# the base dir might include ~ so we need to expand it
base_dir = os.path.expanduser(base_dir)


def list_tasks():
    # Get the project name from the user
    project_name = choose_project()

    if not project_name:
        return

    # Define the project directory path
    project_dir = os.path.join(base_dir, project_name)

    # Ensure the project directory exists
    if not os.path.exists(project_dir):
        print(f"Project '{project_name}' does not exist.")
        return
    tasks_dir = os.path.join(project_dir, "tasks")
    # List all tasks in the project directory
    task_files = [f for f in os.listdir(tasks_dir) if f.endswith(".md")]

    if not task_files:
        print(f"No tasks found in project '{project_name}'.")
        return
    # use fzf to select a task
    selected_task = subprocess.run(
        ["fzf"], input="\n".join(task_files), text=True, stdout=subprocess.PIPE
    )
    # show the task
    if selected_task.returncode == 0:
        task_file = selected_task.stdout.strip()
        with open(os.path.join(tasks_dir, task_file), "r") as task_file:
            print(task_file.read())
    else:
        print("No task selected.")
        return None
    # # Display the list of tasks
    # print(f"Tasks in project '{project_name}':")
    # for task_file in task_files:
    #     print(f"- {task_file[:-3]}")


if __name__ == "__main__":
    list_tasks()
