
#every palnt we create a list and the order is like this: [plant name, sun/rain, how much water in ml, like wind or not(boolean), how much snow in gr will kill them]
plant1=["Aloe vera","sun",200,False,200]
plant2=["Rose","rain",300,False,300]
plant3=["Cactus","sun",150,True,200]

plantlist=[plant1,plant2,plant3]

#input the condition of the weather: 

sunOrClouds,percipitation,wind=input("Please describe the weather conditions, seperated by one space, in the following order: (sun or clouds percipitation number wind(true/false))").split()

print(f' the conditions are: {sunOrClouds},{percipitation},{wind}')

#coverting the variables from str from the input: 
percipitation=int(percipitation)
wind=bool(wind)

if(sunOrClouds=="sun"):
    for plant in plantlist:
            if(plant[1]=="sun"):
                print(f'The {plant[0]} likes {sunOrClouds}')
else: #if the user input clouds
    for plant in plantlist:
            if(plant[1]=="rain"):
                print(f'The {plant[0]} likes {sunOrClouds}')
#checking which plant likes percipitation
for plant in plantlist:
        if(plant[2]>=percipitation):
            print(f'The plant who likes percipitation {percipitation} is: {plant[0]}')

#checking if the plants like winds: 
if(wind==True):
    for plant in plantlist:
            if(plant[3]==True):
                 print(f'The plant who likes wind is: {plant[0]}')
else:
    for plant in plantlist:
            if(plant[3]==False):
                 print(f'The plant who dont like wind is: {plant[0]}')

#checking if the snow amount entered in gr will kill the plants: 

snow=int(input("Enter The amount of snow today: ")) 
for plant in plantlist:
            if(plant[4]>=snow):
                 print(f'The plant who died because of snow is: {plant[0]}')

