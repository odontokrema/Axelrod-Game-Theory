##I am trying to learn how to make a game in Python##
rounds=0
def friedman():
    while rounds<21:
        while oppresponse==True:
            Friedmanresponse=True
        if oppresponse==False:
            while rounds<21:
                Friendmanresponse=False
                return Friedmanresponse
def titfortat():
    titfortatresponse=True
    rounds+=1
    while rounds<21:
        titfortatresponse=oppresponse
    return titfortatresponse
def alwaysaccept():
    return True
def alwaysaccept():
    return False
playerlist=[friedman(),titfortat(), alwaysaccept(), alwaysdefect()]
print("Διάλεξε παίκτες. Friedman 0 TitForTat 1 Always Defect 2 Always Accept 3")
def game(pl1, pl2):
    pl1=playerlist[input("παικτης")]
    pl2=playerlist[input("παικτης")]
    
    
