import yaml


def load_yml_file(file_path: str) -> dict:
    """
    Load the content of a YAML file and return it as a Python dictionary.

    :param file_path: The path to the YAML file.
    :return: The content of the YAML file as a Python dictionary.
    """
     
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
    

def read_file(file_path: str) -> str:
    return