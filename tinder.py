#data type for the 4 users -dictionary
#we'll buils a single user using input function
#we'll start with while loop iterating while the list of users not reaching the end


user1={'name':'keko','gender':'female','age':25,'profession':'singer','favorite tv show':'SteveHarvey','favorite food':'pizza'}
user2={'name':'suma','gender':'male', 'age':30,'profession':'artist','favorite tv show':'one peice','favorite food':'salad'}
user3={'name':'fefo','gender':'female','age':34,'profession':'nail artist','favorite tv show':'naroto','favorite food':'pasta'}
user4={'name':'naro','gender':'male','age':36,'profession':'footballer','favorite tv show':'bleech','favorite food':'salad'}

users_list=[user1,user2,user3,user4]

name,gender,age,profession,favorite_tv_show,favorite_food=input("Enter the following data splitted by one space: name, gender, age, profession, favorite tv show, favorite food: ").split() 

counter=0
while(counter<=len(users_list)-1):
    if(users_list[counter]['gender']!=gender): #if opposite gender there would be a match we continue to chech other terms
        print(f"{users_list[counter]['name']} probably is a good match, well check another terms")
        if(users_list[counter]['favorite tv show']==favorite_tv_show):
            print(f"Wow, {users_list[counter]['name']} likes your favorite tv show, {users_list[counter]['favorite tv show']}, lets chech the other terms!!")
            if(users_list[counter]['age']>=int(age)+2 or users_list[counter]['age']<=int(age)-2):
                #I choose the range of age to be 2 years less or 2 years more
                print(f"{users_list[counter]['name']} is maybe good for you by their age {users_list[counter]['age']}")
                if(users_list[counter]['favorite food'] == favorite_food):
                    print(f"You have the same favourite food too, {users_list[counter]['favorite food']}, you probably be a good match!!")
                    #if the last term has been reached then we print that there is a good match and we should print a message for that
                    print(f"You are a good match with: {users_list[counter]['name']}\n Gender: {users_list[counter]['gender']}\n Favorite food: {users_list[counter]['favorite food']}\n Age: {users_list[counter]['age']}\n Profession:{users_list[counter]['profession']}\n Favorite tv show: {users_list[counter]['favorite tv show']}")
                    break #we need to stop looking for another match
                else:
                    print(f" Unfortunatelly, you and {users_list[counter]['name']} dont like the same food")
                    counter+=1
                    continue
            else:
                print(f"Unfortunatelly, you and {users_list[counter]['name']} not a good match by age")
                counter+=1
                continue
        else:
            print(f"Unfotunatelly, you and {users_list[counter]['name']} not a good match by favourite tv show")
            counter+=1
            continue
    else:
        print(f"Unfotunatelly, you and {users_list[counter]['name']} not a good match by gender!")
        counter+=1
        continue
    
else:
    print(f'You dont have a good match, try again')

        
    
