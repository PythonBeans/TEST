import os, signal
import time

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

def choice():
  choice = None
  while choice != "e" or "E":
    choice = input("Your choice???") 
    if choice == "e" or "E":
      os.kill(os.getpid(), signal.SIGTERM)
    if choice == "add_greeting":
      add_greeting()

def sdownchoice():
  sdownchoice = input("(C)ancel, Exit (w)ith or with(o)ut delay???")
  if sdownchoice != "w" or sdownchoice != "o" or sdownchoice!= "c":
    print("Don't try shit with me!!!")
  while sdownchoice != "w" or sdownchoice != "o" or sdownchoice!= "c":
    sdownchoice = input("(C)ancel, Exit (w)ith or with(o)ut delay???")
    if sdownchoice == "w":
       time.sleep(5)
       os.kill(os.getpid(), signal.SIGTERM)
    if sdownchoice == "o":
       os.kill(os.getpid(), signal.SIGTERM)
    if sdownchoice == "c" or "C":
      choice()
    if sdownchoice != "w" or sdownchoice != "o" or sdownchoice!= "c":
       print("Don't try shit with me!!!")

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
sdownchoice_test()
