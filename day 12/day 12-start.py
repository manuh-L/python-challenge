################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


#local scope... in function


#global.. change global variable 
def increase_enimies():
  global enemies
  enemies += 1
  print(enemies)
  
#outra forma de mudar valor de varivel global sem chamar ou usar global

def increase_enimies():
  return enemies + 1

enemies = increase_enemies()
  