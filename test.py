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
  os.kill(os.getpid(), signal.SIGTERM) 
print(test())
print(name())
print("Last step...")
print("Feierabend")
print("Test vom Gemini")
print(close())

