import random

Hard=[]
Ai=0
User=0

TUser=0
TAi=0

def easyAI(x):
    x=int(x)
    Hard.append(x)
    a=random.randint(0,10)
    if a==0:
        return mediumAI(x)
    else:
        if x==1:
            print("\nAI: Scissor\n")
            return 3
        elif x==2:
            print("\nAI: Rock\n")
            return 1
        elif x==3:
            print("\nAI: Paper\n")
            return 2
    
def mediumAI(x):
    x=int(x)
    Hard.append(x)
    d=random.choice((1,2,3))
    if d==1:
        print("\nAI: Rock\n")
    elif d==2:
        print("\nAI: Paper\n")
    elif d==3:
        print("\nAI: Scissor\n")
    return d


def impossibleAI(x):
    x=int(x)
    Hard.append(x)
    if x==1:
        print("\nAI: Paper\n")
        return 2
    elif x==2:
        print("\nAI: Scissor\n")
        return 3
    elif x==3:
        print("\nAI: Rock\n")
        return 1

def hardAI(x):
    x=int(x)
    global Hard
    if len(Hard)<=3:
        return easyAI(x)
    elif len(Hard)<=6:
        return mediumAI(x)
    else:
        return impossibleAI(Hard.pop(0))

def score(x,y):#x->Player y->AI
    global User,Ai
    if x==1 and y==1:  #y==1
        return "Tie\n"
    elif x==2 and y==1:
        User+=1
        return "Player Won\n"
    elif x==3 and y==1:
        Ai+=1
        return "AI Won\n"
    elif x==1 and y==2:#y==2
        Ai+=1
        return "AI Won\n"
    elif x==2 and y==2:
        return "Tie\n"
    elif x==3 and y==2:
        User+=1
        return "Player Won\n"
    elif x==1 and y==3:#y==3
        User+=1
        return "Player Won\n"
    elif x==2 and y==3:
        Ai+=1
        return "AI Won\n"
    elif x==3 and y==3:
        return "Tie\n"
    else:
        return None

def _main_():
    global User,Ai,TAi,TUser
    print("\nROCK PAPER SCISSOR\n","="*16,"\n")
    while True:
        TUser+=User
        TAi+=Ai
        b=0
        Ai=0
        User=0
        print("Choose your AI level\n1)Easy\n2)Medium\n3)Hard\n4)Impossible\n5)Exit\n")
        inp1=str(input("Your choice:"))
        while True:
            if inp1=="1" or inp1.lower()=="easy" or inp1.lower()=="1)easy":
                while b<10:
                    print("1)Stone\n2)Paper\n3)Scissor")
                    inp2=int(input("Enter your choice number:"))
                    print(score(inp2,easyAI(inp2)))
                    b+=1
                print("\n==Game Over==\nPlayer | AI\n  ",User," | ",Ai)
                break
            elif inp1=="2" or inp1.lower()=="medium" or inp1.lower()=="2)medium":
                while b<10:
                    print("1)Stone\n2)Paper\n3)Scissor")
                    inp2=int(input("Enter your choice number:"))
                    print(score(inp2,mediumAI (inp2)))
                    b+=1
                print("\n==Game Over==\nPlayer | AI\n  ",User," | ",Ai)
                break
            elif inp1=="3" or inp1.lower()=="hard" or inp1.lower()=="3)hard":
                while b<10:
                    print("1)Stone\n2)Paper\n3)Scissor")
                    inp2=int(input("Enter your choice number:"))
                    print(score(inp2,hardAI(inp2)))
                    b+=1
                print("\n==Game Over==\nPlayer | AI\n  ",User," | ",Ai)
                break
            elif inp1=="4" or inp1.lower()=="impossible" or inp1.lower()=="4)impossible":
                while b<10:
                    print("1)Stone\n2)Paper\n3)Scissor")
                    inp2=int(input("Enter your choice number:"))
                    print(score(inp2,impossibleAI(inp2)))
                    b+=1
                print("\n==Game Over==\nPlayer | AI\n  ",User," | ",Ai)
                break
            elif inp1=="5" or inp1.lower()=="exit" or inp1.lower()=="5)exit":
                print("\n==Game Over==\nPlayer | AI\n  ",User," | ",Ai)
                break
        if inp1=="1" or inp1.lower()=="easy" or inp1.lower()=="1)easy" or\
            inp1=="2" or inp1.lower()=="medium" or inp1.lower()=="2)medium" or\
                inp1=="3" or inp1.lower()=="hard" or inp1.lower()=="3)hard" or\
                    inp1=="4" or inp1.lower()=="impossible" or inp1.lower()=="4)impossible":
            continue
        elif inp1=="5" or inp1.lower()=="exit" or inp1.lower()=="5)exit":
            print("\n","="*10)
            print("\n==Total==\nPlayer | AI\n  ",TUser," | ",TAi)
            if TUser==TAi:
                print("\nDRAW\n")
            elif TUser>TAi:
                print("\nUser is the WINNER!\n")
            else:
                print("\nAI is the WINNER!\n")
            break
        else:
            print("\nInvalid Input\n")

_main_()