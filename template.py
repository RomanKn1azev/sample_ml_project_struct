import os
import logging


from pathlib import Path


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


def create_ml_project_struct(path_to_root: str, project_name: str, list_of_files: list):
    """
    Create a project structure for a machine learning project.

    Args:
        project_name (str): The name of the project.
        list_of_files (list): A list of files to include in the project.
    """

    project_dir = os.path.join(path_to_root, project_name)
    os.makedirs(project_dir, exist_ok=True)

    for file_path in list_of_files:
        file_path = Path(file_path)
        filedir, filename = os.path.split(file_path)

        if filedir != "":
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating directory:{filedir} for the file {filename}")


        if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
            with open(file_path,'w') as f:
                pass
                logging.info(f"Creating empty file: {file_path}")

        else:
            logging.info(f"{filename} is already exists")


def main():
    create_ml_project_struct()
    ...


if __name__ == "__main__":
    main()


# project_name = "textSummarizer"


# list_of_files = [
#     ".github/workflows/.gitkeep",
#     f"src/{project_name}/__init__.py",
#     f"src/{project_name}/conponents/__init__.py",
#     f"src/{project_name}/utils/__init__.py",
#     f"src/{project_name}/utils/common.py",
#     f"src/{project_name}/logging/__init__.py",
#     f"src/{project_name}/config/__init__.py",
#     f"src/{project_name}/config/configuration.py",
#     f"src/{project_name}/pipeline/__init__.py",
#     f"src/{project_name}/entity/__init__.py",
#     f"src/{project_name}/constants/__init__.py",
#     "config/config.yaml",
#     "params.yaml",
#     "app.py",
#     "main.py",
#     "Dockerfile",
#     "requirements.txt",
#     "setup.py",
#     "research/trials.ipynb",
# ]


