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
  return " "
test()
print(name())
print("Last step...")
print("Feierabend")
print("Test vom Gemini")
print("Hello from the Beans Corporation Terminaltron CE!!!") 
print(close())
sdownchoice = input("Exit (w)ith or with(o)ut delay???")
while sdownchoice != "w" or "o":
  if sdownchoice == "w":
     time.sleep(5)
     os.kill(os.getpid(), signal.SIGTERM)
  if sdownchoice == "o":
     os.kill(os.getpid(), signal.SIGTERM)
  else:
     print("Don't try shit with me!!!")


