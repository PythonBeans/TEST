import os, signal
import time
import sys

def exit():
  print("Exiting...")
  sys.exit(0)

def test():
  var = input("Zahl ") 
  if int(var) == 1:
    return "1 gedrueckt"
  else:
    print("was anderes gedrueckt")
    time.sleep(3)
    os.kill(os.getpid(), signal.SIGTERM) 

def name():
  name = input("Username: ")
  if name == "Beans" or name == "Justin":
    return "Welcome, " + name
  else:
    print("You are not welcome!!!")
    time.sleep(3)
    os.kill(os.getpid(), signal.SIGTERM)

def close():
  password = input("Your password: ")
  while password != "Python":
    password = input("Your Password: ") 

def add_greeting():
  lst = input("Namelist???: ")
  lst = lst.split(", ")
  print("Your list:")
  print(lst)
  time.sleep(3)
  for name in range(len(lst)):
    lst[name] = "Hello, " + lst[name] + "!"
    print()
    print(lst[name])
    time.sleep(1)
  print()
  print("--------------")
  time.sleep(1)
  print("Your new list:")
  time.sleep(2)
  print()
  print(lst)
  print("--------------")
  print()

#def p_choice():
#  choice = None
#  while choice != "e" or "E":
#    choice = input("Your choice??? ") 
#    if choice == "e" or "E":
#      os.kill(os.getpid(), signal.SIGTERM)
#    if choice == "add_greeting":
#      add_greeting()

def sdownchoice():
  def choicer():
    choice_tab = []
    choice_tab.append(1)
    for sdownchoice in choice_tab:
      sdownchoice = input("(C)ancel, Exit (w)ith or with(o)ut delay??? ")
      if sdownchoice == "w":
        time.sleep(5)
        exit()
      elif sdownchoice == "o":
        exit()
      elif sdownchoice == "c" or sdownchoice == "C":
        test_p_choice()
      elif sdownchoice != "w" or sdownchoice != "o" or sdownchoice!= "c":
        print("Don't try shit with me!!!")
        choicer()
  choicer()

#Debug-Area
#----------

#test()
#print(name())
#print("Last step...")
#print("Feierabend")
#print("Test vom Gemini")
#print("Hello from the Beans Corporation Terminaltron CE!!!") 
#close()
#sdownchoice()
#choice()
#p_choice()
#Example
#-------

def sdownchoice_test():
  def choicer():
    choice_tab = []
    choice_tab.append(1)
    for choice in choice_tab:
      choice = input("Gib mal bitte was ein (a, b, c): ")
      if choice == "a":
        print("a gedrückt")
      elif choice == "b":
        print("b gedrückt")
      elif choice == "c":
        print("c gedrückt")
      else:
        choicer()
  choicer()
#sdownchoice_test()

#p_choice von while loop umschreiben

def p_choice():
  choicetab = []
  def choicer():
    choicetab.append(1)
    for choice in choicetab:
      choice = input("Your choice???(e, add_greeting): ") 
      if choice == "e" or choice == "E":
        #os.kill(os.getpid(), signal.SIGTERM)
        exit()
      elif choice == "add_greeting":
        add_greeting()
        choicer()
      elif choice == "t":
        print("Test erfolgreich")
        choicer()
      else:
        print("Try again")
        choicer()
  choicer()
#p_choice()

def test_p_choice():
  choice = None
  while choice != "e" or choice != "E" or choice != "add_greeting":
    choice = input("Your choice???(e, add_greeting): ")
    if choice == "e" or choice == "E":
      sdownchoice()
    elif choice == "add_greeting":
      add_greeting()
    else:
      print("Try again")
test_p_choice()
