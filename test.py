import os, signal
def test():
  var = input("Zahl ")
  if var == 1:
    return "1 gedrueckt"
  else:
    print("was anderes gedrueckt")
    sleep(3)
    os.kill(os.getpid(), signal.SIGTERM) 
def name():
  name = input("Username: ")
  if name == "Beans" or name == "Justin":
    return "Welcome, " + name
  else:
    return "You are not welcome!!!"
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

