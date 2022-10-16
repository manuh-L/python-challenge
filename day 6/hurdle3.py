def turn_right():
      turn_left()
      turn_left()
      turn_left()

def move_from_wall():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
    
while (at_goal() != "true" ):
  if(wall_in_front()):
    move_from_wall()

#    if(wall_in_front()):
#        move_from_wall()
        
  else:
        move()
    

