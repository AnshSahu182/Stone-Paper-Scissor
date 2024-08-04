""" Please Enter names with First letter CAPITAL """
import random

list=["stone","paper","scissor"]
computer=random.choice(list)
warrior=str(input().lower())
print("Computer's Choice ::",computer)
print("Yours Choice ::",warrior)


if (warrior=="stone" and computer=="stone"):
   print("It's a Draw")

elif (warrior==" scissor" and computer=="scissor"):
   print("It's a Draw")

elif (warrior=="paper" and computer=="paper"):
   print("It's a Draw")
 
elif (warrior =="stone" and computer==" paper"):
   print("You are wrapped by Paper\nYou lost")
 
elif(warrior=="stone"and computer =="scissor"):
   print("You destroyed the Scissor\nYou Won")
 
 
elif(warrior =="paper" and computer =="stone"):
   print("You wrapped the Stone\nYou Won")
 
elif(warrior =="paper" and computer =="scissor"):
   print("You are cut by Scissor\nYou Lose")
  
 
elif (warrior =="scissor" and computer=="paper"):
   print ("You cut the paper\nYou Won")

elif (warrior =="scissor" and computer =="stone"):
   print("Your Scissor is destroyed by Stone\nYou Won")
 
 
else :
   print("INVALID INPUT")
   print("You can Enter only 3 things which are:\n1.Stone💎\n2.Paper🗞\n3.Scissor✄")