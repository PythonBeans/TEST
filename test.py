import os, signal
def test(var):
  if var == 1:
    return "1 gedrückt"
  else:
    os.kill(os.getpid(), signal.SIGTERM) 
def name():
  name = input("Your name?: ")
  if name == "Beans" or name == "Justin":
    return "Welcome, " + name
  else:
    return "You are not welcome!!!"
def close():
  password = input("Your Password: ")
  while password != "Python":
    password = input("Your Password: ")
  os.kill(os.getpid(), signal.SIGTERM) 
print(test(int(input())))
print(name())
print(close())

