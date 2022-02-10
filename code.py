import random

def game(comp,you):
    if comp==you:
        return None
    elif comp=="r":
        if you=="p":
            return True
        elif you=="s":
            return False
    elif comp=="p":
        if you=="s":
            return True
        elif you=="r":
            return False
    elif comp=="s":
        if you=="r":
            return True
        elif you=="p":
            return False


print("computers turn: rock(r),paper(p),scissors(s)")
randomNo= random.randint(1,3)
if randomNo==1:
    comp="r"
elif randomNo==2:
    comp="p"
elif randomNo==3:
    comp="s"
you= input("your turn: rock(r),paper(p),scissors(s)")
print("\n")
a=game(comp,you)
if a==None:
    print("the game is tied")
elif a==True:
    print("You Won!")
else:
    print("You Lost")
   
print(f"computer chose {comp}")
