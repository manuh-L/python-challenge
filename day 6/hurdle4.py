#http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
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
    turn_left()
#    move()
#    turn_right()
    while(wall_on_right() and at_goal() != "true"):
        move()
        if(wall_on_right() != "true"):
            turn_right()
            move()
            turn_right()
        elif(wall_in_front() or front_is_clear() != "true"):
            turn_left()


            
        
        
  else:
      move()