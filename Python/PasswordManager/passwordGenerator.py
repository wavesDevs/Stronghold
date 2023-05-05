#wavesDev password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def pass_gen():

  # # this generator used to ask the user for input in console like this
  # nr_letters= int(input("How many letters would you like to use?\n")) 
  # nr_symbols = int(input(f"How many symbols?\n"))
  # nr_numbers = int(input(f"And finally, how many numbers?\n"))
  
  # #due to moving to GUI implementation, and for the sake of simplying development, i am hard coding these numbers   
  nr_letters = 12
  nr_symbols = 4
  nr_numbers = 4

#Password Generation Logic
  strPass = ''
  password = []

  for i in range (1, nr_letters+1):
    randletter = random.randint(0,51)
    password.append(letters[randletter])

  for i in range (1, nr_symbols+1):
    randsym = random.randint(0,8)
    password.append(symbols[randsym])

  for i in range (1, nr_numbers+1):
    randno = random.randint(0,9)
    password.append(numbers[randno])

  scramble = random.sample(password, len(password))

  return strPass.join(scramble)