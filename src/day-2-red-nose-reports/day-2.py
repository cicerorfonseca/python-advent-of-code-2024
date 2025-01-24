import os
import sys

# Add the root directory to sys.path dynamically
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import helpers
from utils import read_input

def compute_input(input_content:list[str]) -> list[list[int]]:
  """Parse input lines and removes spaces from both sides
  then casts each string character into integers.

  *** Must be refactored for improved time complexity. Nested FOR should be avoided here.

  Args:
    input_content (list[str]): List of strings containing space-separated numbers

  Returns:
    list[list[int]]: A list of lists containing integers
  """
  computed_input = []

  for line in input_content:
    formatted_line = []

    line = line.strip().split()

    for char in line:
      formatted_line.append(int(char))
    
    computed_input.append(formatted_line)

  return computed_input

def compute_safe_reports(reports: list[list[int]]) -> int:
  """Loops through all reports in the list and sums up the total of safe reports

  Args:
    reports (list[int]): the list of reports

  Returns:
    int: The total number of safe reports
  """
  safe_reports = 0

  for report in reports:
    if (is_report_safe(report)):
      safe_reports += 1

  return safe_reports

def is_report_safe(report: list[int]) -> bool:
  """Runs through the report and verifies if the numbers diff is between 1 and 3
  and if the levels are all decreasing or all increasing

  Args:
    report (list[int]): List of integers representing the report

  Returns:
    bool: True if the report is safe, False otherwise
  """
  try:
    for i in range(len(report) - 1):
      if not 1 <= abs(report[i] - report[i + 1]) <= 3: # Safe as the levels are decreasing by 1 or 3
        return False
      
      if i > 0: # Start verification from second number
        if ((report[i] > report[i + 1] and report[i] >= report[i - 1]) or # All levels are decreasing
          (report[i] < report[i + 1] and report[i] <= report[i - 1])): # All levels are increasing
            return False
      
    return True
      
  except Exception as e:
    print(e)

if __name__ == "__main__":
  dirname = os.path.dirname(__file__)
  FILE_NAME = "./input.txt" # 663
  FILE_NAME_EXAMPLE = "./input-example.txt" # 2
  FILE_PATH = os.path.join(dirname, FILE_NAME)

  try:
    input_content = read_input(FILE_PATH)
    computed_input = compute_input(input_content)
    result = compute_safe_reports(computed_input)

    print(result)
  except Exception as e:
    print(f"Program failed: {e}")
  
    exit(1)
