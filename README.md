# tik - a Project Management Tool with Git Integration

## THIS IS WORK IN PROGRESS AND NOT YET FUNCTIONAL

This project is a simple open-source project management tool that leverages Git for synchronization and task tracking. It allows users to manage tasks within projects using Markdown files, with a focus on simplicity and ease of use.

## Features

- **Project Creation**: Users can create projects, each represented as a directory with a Git repository and a `project.md` file for project-specific information.

- **Task Management**: Tasks are represented as Markdown files within project directories. The tool follows a predefined task template for consistency.

- **Interactive Project Selection**: Users can choose a project from a list when adding tasks to ensure tasks are associated with the correct project.

- **Task Numbering**: Tasks are automatically numbered within each project for easy reference and organization.

- **Git Integration**(WIP): The tool abstracts Git operations in the background, making it easy for users to work with version control without needing Git expertise.

## Usage

To use the project management tool:

1. Clone this repository.

2. Install the necessary dependencies using `conda env create -f environment.yml`.

3. Run the `create_project.py` script to create a project. The script guides users through project creation, and projects are stored as directories with a `project.md` file for project-specific information.

4. Run the `add_task.py` script to create tasks within projects. The script guides users through task creation, and tasks are stored as Markdown files in project directories.

## Task Template

The template for tasks in in `task_template.md`.

## Dependencies

- Python 3.x
- Git (for version control and remote repositories)
- fzf (for interactive selection)

## Contributing

Contributions to the Project Management Tool are welcome! Feel free to open issues or pull requests on the [GitHub repository](https://github.com/vvhg1/tik.git).

## License

This project is licensed under the GNU General Public License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

Inspired by the need for a simple project management tool that integrates with Git.

Happy project management!
