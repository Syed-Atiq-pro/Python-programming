import random

def game():
    score = random.randint(1,63) 
    with open("hiscore.txt","r") as f:
        hiscore = f.read()
        if  hiscore != "" :
            hiscore = int(hiscore)
           
        else:   
          hiscore = 0
    print(score)
    if (score > hiscore ):
        with open("hiscore.txt","w") as s:
            s.write(str(score))
      
game()

