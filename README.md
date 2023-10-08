# tik - A Project Management Tool with Git Integration

<!-- ![Tik Logo](logo.png) -->

**Note: This project is currently a work in progress and is not yet fully functional. In fact it's in a very early stage of development. Feel free to contribute!**

tik is (going to be) a simple yet powerful open-source project management tool designed to streamline project and task management while seamlessly integrating with Git for version control. With tik, you can efficiently organize tasks within projects using Markdown files, prioritizing simplicity and ease of use.

## Features

- **Project Creation**: Easily create and manage projects, each represented as a dedicated directory equipped with a Git repository and a `project.md` file for detailed project-specific information.

- **Effortless Task Management**: Tasks are represented as Markdown files within project directories. tik follows a predefined task template for consistency, making it simple to create and organize tasks.

- **Interactive Project Selection**: When adding tasks, tik allows users to interactively select the project, ensuring that tasks are correctly associated with the appropriate project.

- **Automatic Task Numbering**: Tasks are automatically numbered within each project, simplifying reference and organization as your projects grow.

- **Git Integration** (Work in Progress): tik abstracts Git operations into the background, enabling users to work with version control without requiring in-depth Git expertise.

## Usage

To utilize the project management capabilities of tik:

1. **Clone the Repository**: Begin by cloning this repository to your local machine.

2. **Install Dependencies**: Install the necessary dependencies using the provided `environment.yml` file with `conda env create -f environment.yml`.

3. **Create a Project**: Run the `create_project.py` script to create a new project. The script will guide you through the project creation process, storing project-related information in a directory equipped with a `project.md` file.

4. **Add Tasks**: Utilize the `add_task.py` script to create tasks within projects. The script will walk you through the task creation process, with tasks stored as Markdown files within project directories.

## Task Template

To maintain consistency, tasks within tik adhere to the template outlined in `task_template.md`.

## Dependencies

- Python 3.x
- Git (for version control and remote repositories)
- fzf (for interactive selection)

## Contributing

Contributions to the tik Project Management Tool are highly encouraged and welcome! If you'd like to get involved, feel free to open issues or submit pull requests on the [GitHub repository](https://github.com/vvhg1/tik.git).

## License

tik is licensed under the GNU General Public License (GPL). For full licensing details, refer to the [LICENSE.md](LICENSE.md) file.

## Acknowledgments

tik was inspired by the need for a straightforward project management tool that seamlessly integrates with Git.

Happy project management with tik!
