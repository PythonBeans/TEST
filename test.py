def test(var):
  if var == 1:
    return "1 gedrückt"
  else:
    return exit()
def name():
  name = input("Your name?: ")
  if name == "Beans" or name == "Justin":
    return "Welcome, " + name
  else:
    return "You are not welcome!!!"
print(test(int(input())))
print(name())

