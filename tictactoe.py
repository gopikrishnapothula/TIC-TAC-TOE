
def board():
    r1="|{}|{}|{}|".format(bd[0],bd[1],bd[2])
    r2="|{}|{}|{}|".format(bd[3],bd[4],bd[5])
    r3="|{}|{}|{}|".format(bd[6],bd[7],bd[8])
    print(r1)
    print(r2)
    print(r3)
def player1mov():
    print("{} turn Enter number 1 to 9 : ".format(p1))
    n=int(input())
    if n>=1 and n<=9:
        
        if bd[n-1]!="X" and bd[n-1]!="O":
            bd[n-1]='X'
            
            board()
        else :
            print("already filled")
            player1mov()
    else :
        print("Enter valid number")
        player1mov()
def player2mov():
    print("{} turn Enter number 1 to 9 : ".format(p2))
    n=int(input())
    if n>=1 and n<=9:
        
        if bd[n-1]!="X" and bd[n-1]!="O":
            bd[n-1]='O'
            
            board()
        else :
            print("already filled")
            player2mov()
    else :
        print("Enter valid number")
        player2mov()

def isp1win():
    if(bd[0]==bd[3]==bd[6]=='X' or bd[1]==bd[4]==bd[7]=='X' or bd[2]==bd[5]==bd[8]=='X' or bd[0]==bd[1]==bd[2]=='X' or bd[3]==bd[4]==bd[5]=='X' or bd[6]==bd[7]==bd[8]=='X' or bd[0]==bd[4]==bd[8]=='X' or bd[2]==bd[4]==bd[6]=='X'):
        return True
def isp2win():
    if(bd[0]==bd[3]==bd[6]=='O' or bd[1]==bd[4]==bd[7]=='O' or bd[2]==bd[5]==bd[8]=='O' or bd[0]==bd[1]==bd[2]=='O' or bd[3]==bd[4]==bd[5]=='O' or bd[6]==bd[7]==bd[8]=='O' or bd[0]==bd[4]==bd[8]=='O' or bd[2]==bd[4]==bd[6]=='O'):
        return True

def isdraw():
    if " " not in bd:
        return True


import sys
n=[i for i in range(1,10)]
bd=[" " for i in range(0,9)]
print("TIC-TAC-TOE GAME")
p1=input("Enter player1 name : ")
p2=input("Enter player2 name : ")
board()

while(True) :
    player1mov()
    if(isp1win()):
        print("{} wins".format(p1))
        sys.exit()
    if(isdraw()):
        print("Its  tie")
        sys.exit()
    player2mov()
    if(isp2win()):
        print("{} wins".format(p2))
        sys.exit()
    if(isdraw()):
        print("Its  tie")
        sys.exit()
    
    
