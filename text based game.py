
print("Hello world")
name = input("what is your name   ")
print ("hi", name)
adventure = input("do you want to go on a adventure?")
if adventure == "yes":
   print("awesome")
   q1 =  input("You begin your adventure. You see a big rocket do you get on it?")
   if q1 == "yes":
      print("Rock on")
      print("You go inside the rocket and turn it on you have begun your adventure")
      for x in range(10):
       print("")
      print("you have ben sleaping for 1 hour there are beping noises all around you")
      q2 = input("what do you do")
      print("You are sucesfull")
      print("Youre quick thinking and", q2,"saved you")
   elif q1 == "no":
      print("Game over") 
   
elif adventure == "no":
   print("game over")
