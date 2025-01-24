import os
import sys

# Add the root directory to sys.path dynamically
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import helpers
from utils import read_input

def compute_input(input_content: list[str]) -> tuple[list[int], list[int]]:
    """Parse input lines and split numbers into two lists

    Args:
        input_content (list[str]): List of strings containing space-separated numbers

    Returns:
        tuple[list[int], list[int]]: Tuple containing two lists of integers:
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

def calculate_similarity(number_pairs: tuple[list[int], list[int]]) -> int:
    """Calculate the similarity score by adding up each number from the left side
    after multiplying it by the number of times the number appears in the right side

    Args:
        number_pairs (tuple[list[int], list[int]]): Tuple containing two lists of integers:
            - First list: Left numbers to be paired
            - Second list: Right numbers to be paired

    Returns:
        int: Sum of the similarity score of each number on the left list
    """
    left_nums, right_nums = number_pairs
    right_num_counts = {}

    for right_num in right_nums:
        right_num_counts[right_num] = right_num_counts.get(right_num, 0) + 1

    similarity_score = sum(
        left_num * right_num_counts.get(left_num, 0) for left_num in left_nums
    )

    return similarity_score


if __name__ == "__main__":
    dirname = os.path.dirname(__file__)
    FILE_NAME = "./input.txt"  # pt1: 3574690 pt2: 22565391
    FILE_NAME_EXAMPLE = "/input-example.txt"  # 11
    FILE_PATH = os.path.join(dirname, FILE_NAME)

    try:
        input_content = read_input(FILE_PATH)
        number_pairs = compute_input(input_content)
        result = calculate_total(number_pairs)
        similarity_score = calculate_similarity(number_pairs)

        print(result)
        print(similarity_score)
    except Exception as e:
        print(f"Program failed: {e}")

        exit(1)
