def read_input(file_path: str) -> list[str]:
    """Read lines from a file and return the content as a list

    Args:
      file_path (str): Path to the input file

    Returns:
      list[str]: List of strings, each item as a line from the file

    Raises:
      FileNotFoundError: If the file does not exist
      PermissionError: If the file cannot be accessed
    """
    try:
        with open(file_path) as file:
            return file.readlines()
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error reading file {file_path}: {e}")

        raise
