def turn_right():
      turn_left()
      turn_left()
      turn_left()

def hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

    
while (at_goal() != "true"):
    hurdle()

#while not at_goal():
#    hurdle()
