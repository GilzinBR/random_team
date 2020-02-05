# The plan is:
# 1- I have a list of teams and a empty list
# 2- I will pick one random position of the team list
# 3- The team that is in this position I will add on the empty list
# 4- The team that was in this position now will change to 'Check'. This way I dont pick this position again
# 5- Now the empty list is a of the teams in a random position. And the original list is only with 'Check'

import random

team_list = ['Flamengo', 'Barcelona', 'Liverpool', 'Real Madrid', 'Juventus', 'Botafogo']
random_team_list = []
count = 0
list_size = len(team_list) #How many teams are in this list

while count < list_size:
    random_position = random.randint(0, list_size-1) #random position in the list
    
    if team_list[random_position] != 'Check':
        
        random_team_list.append(team_list[random_position])
        
        team_list[random_position] = 'Check'
        
        count += 1
        
print(random_team_list)
