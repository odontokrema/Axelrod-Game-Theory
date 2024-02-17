#I am trying to learn how to make a game in Python
rounds=0

def friedman():
    while rounds<21:
        while oppresponse==True:
            Friedmanresponse=True
        if oppresponse==False:
            while rounds<21:
                Friendmanresponse=False
                return Friedmanresponse
#True is cooperate and false is defect
def titfortat():
    titfortatresponse=True
    rounds+=1
    while rounds<21:
        titfortatresponse=oppresponse
    return titfortatresponse
def alwaysaccept():
    alwaysacceptresponse=True
    return alwaysacceptresponse
def alwaysdefect():
    alwaysdefectresponse=False
    return alwaysdefectresponse
playerlist=[friedman(),titfortat(), alwaysaccept(), alwaysdefect()]
print("Διάλεξε παίκτες. Friedman 0 TitForTat 1 Always Defect 2 Always Accept 3")
def game(pl1, pl2):
    pl1=playerlist[input("παικτης")]
    pl2=playerlist[input("παικτης")]
    
    
    resultpl1=pl1
    resultpl2=pl2
    points1=0
    points2=0
    if resultpl1==True and resultpl2==True:
        points1+=3
        points2+=3
    elif resultpl1==True and resultpl2==False:
        points2+=5
    elif resultpl1==False and resultpl1==True:
        points1+=5
    else:
        points1+=1
        points2+=1


    
    
