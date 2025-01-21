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


def compute_input(input_content: list[str]) -> tuple[list[int], list[int]]:
    """Parse input lines and split numbers into two lists

    Args:
        input_content (list[str]): List of strings containing space-separated numbers

    Returns:
        Tuple[list[int], list[int]]: Tuple containing two lists of integers:
            - First list: Left values parsed from input
            - Second list: Right values parsed from input
    """
    left_values = []
    right_values = []

    for line in input_content:
        line = line.strip().split()
        left_values.append(int(line[0]))
        right_values.append(int(line[1]))

    return (left_values, right_values)


def calculate_total(number_pairs: tuple[list[int], list[int]]) -> int:
    """Calculate total absolute difference between sorted pairs

    Args:
        number_pairs (tuple[list[int], list[int]]): Tuple containing two lists of integers:
            - First list: Left numbers to be paired
            - Second list: Right numbers to be paired

    Returns:
        int: Sum of absolute differences between paired numbers
    """
    left_nums, right_nums = number_pairs
    left_nums.sort()
    right_nums.sort()

    return sum(abs(left - right) for left, right in zip(left_nums, right_nums))


if __name__ == "__main__":
    FILE_NAME = "input.txt"  # 3574690
    FILENAME_EXAMPLE = "input-example.txt"  # 11

    try:
        input_content = read_input(FILE_NAME)
        number_pairs = compute_input(input_content)
        result = calculate_total(number_pairs)
        print(result)
    except Exception as e:
        print(f"Program failed: {e}")
        exit(1)
