import math
from itertools import permutations

# def get_perms(word, combos=[]):
  

  # letters = word.split("")
  # if combos == []:
  #   combos = ["" for i in word]

  # added_index = 0
  # while added_index < len(combos):
  #   for i in range(len(combos) / len(letters)):
  #     combo[i + added_index] += letters[i]


def get_file_lines(filename='/usr/share/dict/words'):
    """Return a list of strings on separate lines in the given text file with
    any leading and trailing whitespace characters removed from each line."""
    # Open file and remove whitespace from each line
    with open(filename) as file:
        lines = [line.strip() for line in file]
    return lines

def jumble(word):
  combos = list(permutations(word))
  for i, l in enumerate(combos):
    combos[i] = "".join(l)
  combos = set(combos)
  

  dicto = set(get_file_lines())
  return combos.intersection(dicto)

  

  
  
  

  
  



print(list(jumble("tefon")))
