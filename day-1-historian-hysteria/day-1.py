file_name = 'input.txt' # 3574690
file_name_example = 'input.txt' # 11

# Reads the file content and returns it as a list
def read_input(file_name: str) -> list[str]:
  try:
    with open(file_name) as file:
      data = file.readlines()

      return data
  except Exception as e:
    print(e)

# Formats and joins all lines then splits the numbers between two lists
def compute_input(input_content: list[str]) -> tuple[list[int], list[int]]:
  list_l = []
  list_r = []

  for line in input_content:
    # Join all numbers and split them into indexes
    line = ''.join(line).split()
    # Append number to each list
    list_l.append(int(line[1]))
    list_r.append(int(line[0]))

  return (list_r, list_l)

def calculate_total(lists: tuple[list[int],list[int]]) -> int:
  lists[0].sort()
  lists[1].sort()
  total = 0

  for i, val_l in enumerate(lists[0]):
      total += abs(val_l - lists[1][i])

  return total

# Main
if __name__=="__main__":
  input_content = read_input(file_name)
  lists = compute_input(input_content)

  print(calculate_total(lists))
