#2 players?
#player1
pokemon1={'name':'charizard', 'level': 0, 'strength':5, 'speed':2, 'type':'fire', 'life':120}
pokemon2={'name':'squirtle', 'level': 0, 'strength':6, 'speed':1, 'type':'water', 'life':120}
pokemon3={'name':'caterpie', 'level': 0, 'strength':3, 'speed':1, 'type':'earth', 'life':120}
pokemon4={'name':'pidgeot', 'level': 0, 'strength':3, 'speed':2, 'type':'wind', 'life':120}
pokemon5={'name':'vulpix', 'level': 0, 'strength':2, 'speed':1, 'type':'fire', 'life':120}
#player2
pokemon6={'name':'ninetales', 'level': 0, 'strength':4, 'speed':2, 'type':'fire', 'life':120}
pokemon7={'name':'blastoise', 'level': 0, 'strength':5, 'speed':2, 'type':'water', 'life':120}
pokemon8={'name':'primeape', 'level': 0, 'strength':4, 'speed':3, 'type':'earth', 'life':120}
pokemon9={'name':'machamp', 'level': 0, 'strength':5, 'speed':2, 'type':'wind', 'life':120}
pokemon10={'name':'arcanine', 'level': 0, 'strength':5, 'speed':3, 'type':'fire', 'life':120}
player1=[pokemon1,pokemon2,pokemon3,pokemon4,pokemon5]
player2=[pokemon6,pokemon7,pokemon8,pokemon9,pokemon10]

import random
#the while loop will operate the game, if one of them get only one pokemon, we'll move to another battle if he lose he'll lose the whole game
while(len(player1)>0 and len(player2)>0):
    for pok in player1:
        pok['speed']+=random.randint(1,20)
    for pok in player2:
        pok['speed']+=random.randint(1,20)
   #chose the pokemon:
    maxSpeed1=1
    maxSpeed2=1
    for pok in player1:
        if(pok['speed']>maxSpeed1):
            maxSpeed1=pok['speed']
            name1=pok['name']
            type1=pok['type']
            life1=120
            strength1=pok['strength']
    for pok in player2:
        if(pok['speed']>maxSpeed2):
            maxSpeed2=pok['speed']
            name2=pok['name']
            type2=pok['type']
            life2=120
            strength2=pok['strength']
    print(f'pokemon {name1} for player1 had joined the fight against pokemon {name2} for player2 ')
    if(maxSpeed1>maxSpeed2):
        attacker=name1
        defender=name2
    else:
        attacker=name2
        defender=name1
    #setting the type modifier we'll first check what kind of pokemons the players chose: 
    if(type1=='fire'):
        if(type2=='wind'):
            typeMod1=2
            typeMod2=1
        else:
            typeMod1=1
            typeMod2=2
    elif(type1=='water'):
        if(type2=='wind'):
            typeMod1=1
            typeMod2=2
        else:
            typeMod1=2
            typeMod2=1
    elif(type1=='earth'):
        if(type2=='water'):
            typeMod1=1
            typeMod2=2
        else:
            typeMod1=2
            typeMod2=1
    else: #type1=wind
        if(type2=='water'):
            typeMod1=2
            typeMod2=1
        else:
            typeMod1=1
            typeMod2=2
#calculating the damage: 
    damage1=typeMod1*(random.randint(1,20)+strength1)
    damage2=typeMod2*(random.randint(1,20)+strength2)
#what i understand from the question is that the defender who'll be life subtracted by the damage
    while(life1>0 and life2>0):
        if(attacker==name1):
            print(f'pokemon {name1} had attacked pokemon {name2}')
            attacker=name2
            life2-=damage1
        
        elif(attacker==name2):
            print(f'pokemon {name2} had attacked pokemon {name1}')
            attacker=name1
            life1-=damage2
        print(f'pokemon {name1} has a life of {life1}, pokemon {name2} has a life of {life2}')
        

    if(life1<=0): #the name1 pokemon lost 
        for index,value in enumerate(player1):
            if(pok['name']==name1):
                del player1[index]
        print(f'pokemon {name1} -player1 has died')
        print(f'pokemon {name2} -player2 winned')
        
    if(life2<=0):#the name2 pokemon lost
        for index,pok in enumerate(player2):
            if(pok['name']==name2):
                del player2[index]
        print(f'pokemon {name2} -player2 has died')
        print(f'pokemon {name1} -player1 winned')
#print the winner
if(len(player1)>len(player2)):
    print(f' the winner is player1')
else:
    print(f'the winner is player2')
        
        


                    
        
    
        
        
