from random import randint
responses = ["Yes","No","Probably","Maybe","I Don't Think So","Perhaps","It's Possible",
             "Yes, I think so"]
print("Welcome to the Magic 8 ball")

def eight_ball():
  question = input("Ask a question")
  print(responses[randint(0,7)])
  
  while True:
    play = input("Would you like to play again?")  #Y,y for yes and N,n for no
    
    if play=="Y" or play=="y":
      eight_ball()
     elif play=="N" or play=="n":
      break
     else:
      print("I didn't quite catch that")
eight_ball()
