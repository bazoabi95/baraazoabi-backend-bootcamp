#choose classes to build the code
#functions
#list of 20 materails
#the 4 alien delegations will be created as objects

myMaterials=['FXY45','FD45G','AQW67','RTY89','OIU90','MNB09','QWE21','GVZ65','ZXC11','ERT65','MJO09','TYZ00','ZERS0','QMP80','JJK78','POZX6','QAAB7','UVC80','KKO44','YTB88','TY679']

import copy

class AlienDelegation:
    def __init__(self,name,materials,numSuggestions):
        self.name=name
        self.materials=materials
        self.numSuggestions=numSuggestions
        self.initial_suggestions=numSuggestions
        #materials property have to be a list 
    def __str__(self):
        return f'Alein delegation Name: {self.name} \n Needed materials: {self.materials}\n Number of Suggestions: {self.initial_suggestions}\n'
    def get_NumSuggestions(self):
        return self.numSuggestions
    def get_materials(self):
        return(self.materials)
    def set_NumSuggestions(self,newNum):
         self.numSuggestions=newNum
    def get_initialSugg(self):
        return self.initial_suggestions
a1= AlienDelegation("NEMO",['UVC80','KKO44','YTB88','456df','0987e'],4)
a2= AlienDelegation("VEVO",['C80OL','RTY89','OIU90','MNB09','00025'],4)
a3= AlienDelegation("SOLO",['AQW67','RTY89','OIU90','MNB09','QWE21'],5)
a4= AlienDelegation("ROU",['85LKHG','KKK00','YUYHG0','90MGFH','BNM09'],4)

alien_list=[a1,a2,a3,a4]
        
import random    

#the function suggestion will choose for us randomly a material from the materials list above 
def suggestion():
    return (myMaterials[random.randint(0,len(myMaterials)-1)])
#negtiation function will represent negotiation with every alien
def negotiation(alienDelegation):
    
    #def suggestionUsed(): #this function will remove 1 suggestion from the suggestions given in every alien object
        #alienDelegation.set_NumSuggestions(alienDelegation.get_NumSuggestions()-1)

    print(alienDelegation)
    agreed=False #it turns true if the alien agree for the suggestion
    countAgreed=0
    #saving the number of the suggestions in a help var
    sugg_copy=alienDelegation.get_initialSugg()
    #we keep iterating until we finish suggestions for each alien object
    while(sugg_copy >0):
        sug=suggestion()
        print(f' our suggestion is:{sug}')
        for item in alienDelegation.get_materials():
            if item==sug:
                agreed=True
                print(f'Alien agreed to cooperate')
                countAgreed+=1
            if(agreed==False):
                print('Alien didnt agree for our suggestion')
        sugg_copy-=1
        agreed=False #we get it back to false to check the next suggestions
    return countAgreed
    
#now we'll rub through all aliens , and print the final results.

count_convinced_aliens=0
for alien in alien_list:
    convinced_count=negotiation(alien)
    print(f'this alien was convinced by: {convinced_count/alien.get_NumSuggestions()*100}%')
    if(convinced_count>0):
        count_convinced_aliens+=1
print(f'convinced aliens are {count_convinced_aliens/len(alien_list)*100}%')
if(count_convinced_aliens/len(alien_list) >=0.7):
    print('you are successful')
else:
    print('you lose')


#print(a1.get_materials())
#print(negotiation(a1))
#print(negotiation(a1))


    

