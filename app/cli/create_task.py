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
# the base dir might include ~ so we need to expand it
base_dir = os.path.expanduser(base_dir)
logging.info(f"base_dir: {base_dir}")


def create_task():
    # Get the project name from the user
    project_name = choose_project()

    if not project_name:
        return

    # Generate a unique identifier
    unique_id = str(uuid.uuid4())

    # Define the project directory path
    project_dir = os.path.join(base_dir, project_name)
    project_tasks_dir = os.path.join(project_dir, "tasks")

    # get the running ticket number from the project.md file
    with open(os.path.join(project_dir, "project.md"), "r") as project_file:
        # we only need the first line
        first_line = project_file.readline()
        # get the running ticket number
        running_ticket_number = int(first_line.split(":")[1].strip())
        # increment the running ticket number
        running_ticket_number += 1

    # Get task details from the user
    # Get task details from the user
    task_title = input("Enter the task title: ")
    task_storypoints = input("Enter the task story points (if applicable): ")
    # make sure the story points are a number
    while not task_storypoints.strip().isdigit():
        task_storypoints = input("Enter the task story points (if applicable): ")
    task_assignee = input("Enter the task assignee (if applicable): ")
    task_priority = input("Enter the task priority (High/Medium/Low, or custom): ")
    task_status = input(
        "Enter the task status (To Do/In Progress/Completed/Blocked, or custom): "
    )
    task_due_date = input("Enter the task due date (YYYY-MM-DD, if applicable): ")
    task_tags = input("Enter the task tags (comma-separated): ").split(",")
    task_estimated_time = input("Enter the estimated time (e.g., 2 hours): ")
    task_actual_time = input("Enter the actual time (e.g., 1.5 hours): ")
    task_related_issues = input(
        "Enter related issues (comma-separated, e.g., Issue #1, Issue #2): "
    )

    # Create a new task Markdown file
    storypoints_for_filename = f"[{task_storypoints}]_" if task_storypoints else ""
    task_filename = f"#{running_ticket_number}_{storypoints_for_filename}{task_title.replace(' ', '_').lower()}.md"
    task_filepath = os.path.join(project_tasks_dir, task_filename)

    # Create the task file and write task details in Markdown format
    with open(task_filepath, "w") as task_file:
        task_file.write(f"# #{running_ticket_number} {task_title}\n\n")
        task_file.write(f"- **Assignee:** {task_assignee}\n")
        task_file.write(f"- **Priority:** {task_priority}\n")
        task_file.write(f"- **Status:** {task_status}\n")
        task_file.write(f"- **Due Date:** {task_due_date}\n")
        task_file.write(f"- **Tags:** {', '.join(task_tags)}\n")
        task_file.write(f"- **Estimated Time:** {task_estimated_time}\n")
        task_file.write(f"- **Actual Time:** {task_actual_time}\n")
        task_file.write(f"- **Related Issues:** {task_related_issues}\n")
        task_file.write("\n---\n\n")
        task_file.write("## Description\n\n")
        task_file.write(
            "A brief description of the task goes here. This section provides an overview of what needs to be done.\n"
        )
        task_file.write("\n## Steps to Reproduce (if a bug/task report)\n\n")
        task_file.write(
            "If the task involves reproducing a bug or specific steps, list them here.\n\n"
        )
        task_file.write("1. Step 1\n2. Step 2\n3. ...\n")
        task_file.write("\n## Acceptance Criteria\n\n")
        task_file.write(
            "- List specific criteria that need to be met for the task to be considered completed.\n"
        )
        task_file.write("- These criteria should be clear and objective.\n")
        task_file.write("\n## Additional Information\n\n")
        task_file.write(
            "- Any additional notes, context, or information related to the task.\n"
        )
        task_file.write("- Links to external resources, documents, or references.\n")
        task_file.write("\n## Attachments\n\n")
        task_file.write(
            "- Attach relevant files, screenshots, or documents related to the task.\n\n"
        )
        task_file.write("\n---\n\n")
        task_file.write("## Progress\n\n")
        task_file.write(
            "- [ ] To Do\n- [ ] In Progress\n- [ ] Completed\n- [ ] Blocked\n\n"
        )
        task_file.write("\n---\n\n")
        task_file.write("## Comments\n\n")
        task_file.write(
            "- Discussion, updates, and comments related to the task can be added here.\n"
        )

    # if we had successfully created the task file, we can update the project.md file running ticket number
    # overwrite the first line only
    with open(os.path.join(project_dir, "project.md"), "r+") as project_file:
        # read the whole file
        lines = project_file.readlines()
        # go back to the beginning of the file
        project_file.seek(0)
        # write the first line with the updated running ticket number
        project_file.write(f"running ticket number: {running_ticket_number}\n")
        # write the rest of the lines
        project_file.writelines(lines[1:])

    print(f"Task '{task_title}' added to project '{project_name}' successfully!")


if __name__ == "__main__":
    create_task()
