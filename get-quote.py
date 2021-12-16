import random
def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  rnd1 = rnd2 = random.randint(0, last)
  while rnd2 == rnd1:
    rnd2 = random.randint(0, last)

  print(quotes[rnd1][:-1])
  print(quotes[rnd2][:-1])

  return quotes

def add_quote(qt_str):
  """Adds a quote to the file for future printing."""
  f = open("quotes.txt", "a")
  quotes = f.writelines(qt_str + "\n")
  print("The quote was successfully added.")
  f.close()

def ask_add_quote():
  """Asks whether to append a quote to the quotes.txt file.""" 

  # Iterates until it gets a valid response from the user.
  r = "x"
  while r not in ["y", "n"]:
    r = input("Would you like to add a quote? (y/n): ")

  # Processes the previously validated user's response.
  if r == "y":
    qt = input("Write it: ")
    add_quote(qt)
  else:
    pass

if __name__== "__main__":
  primary()
  ask_add_quote()
