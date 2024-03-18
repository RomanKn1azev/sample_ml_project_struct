from argparse import ArgumentParser


def parse_arguments(
        description: str,
        required_arguments: list,
        optional_arguments: list
        ):
    """
    Define and parse command-line arguments using argparse.

    Returns:
        argparse.Namespace: Parsed command-line arguments.
    """
    parser = ArgumentParser(description=description)

    # Required arguments

    for argument_params in required_arguments:
        parser.add_argument(
            **argument_params
        )

    # Optional arguments
    for argument_params in optional_arguments:
        parser.add_argument(
            **argument_params
        )
    
    args = parser.parse_args()

    return args
