from game_data import data
import art 
import random

def find_2_random_person(more_follower):
    person_list = []
    if  more_follower:
        indice = random.randint(0,(len(data)-1))
        while indice == more_follower["list_index"]:
              indices = random.randint(0,(len(data)-1))
        more_follower["person_index"] = "A"   
        person_list.append(more_follower)
        person_list.append(data[indice])
        person_list[1]["person_index"]  = "B" 
        person_list[1]["list_index"]  = indice   
    else:
        indices = random.sample(range(len(data)-1), k=2)
        for indice in indices:
            person_list.append(data[indice])    
        person_list[0]["person_index"]  = "A"  
        person_list[0]["list_index"]  = indices[0]
        person_list[1]["person_index"]  = "B" 
        person_list[1]["list_index"]  = indices[1]
    print(f"compare A: {person_list[0]["name"]} , a {person_list[0]["description"]}, from {person_list[0]["country"]}" )
    print(art.vs)
    print(f"against B: {person_list[1]["name"]} , a {person_list[1]["description"]}, from {person_list[1]["country"]}" )
    return person_list

def copmare(person_list,guess,score): 
    more_follower = {
        'name': '',
        'follower_count': 0,
        'description': '',
        'country': '',
        "person_index":"",
        "indice":0
        }
    should_break = True
    for i in range(0,len(person_list)):
        if person_list[i]["follower_count"] > more_follower["follower_count"]:
            more_follower = person_list[i]
            
    if more_follower["person_index"] == guess:
       score +=1
       should_break= False
       
       
       
    return score, should_break,more_follower  
def vs_game():  
    print(art.logo)
    print("welcome to vs game")
    score = 0
    more_follower = {}
    while True:  
        person_list = find_2_random_person(more_follower) 
        guess = input("who has more followers? type 'A' or 'B': ")  
        score,should_break,more_follower = copmare(person_list,guess,score)
        if should_break ==True:
            print(f"sorry,that was wrong! final score : {score}")
            break
        print(f"you are right! current score : {score}")
        
        
    
vs_game()