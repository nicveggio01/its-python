current_users:list=["stefano", "lisa", "sara", "max", "giorgio"] 
new_users: list=["paola", "giovanni", "stefano", "sara", "francesca"] 

for i in new_users:
    if i in current_users:
        print("the username is already used, please choose another one!")
    
else:
    print("the username is not available")
          
current_users:list=["stefano", "lisa", "sara", "max", "giorgio"] 

for i in current_users:
    i.upper()
    print("current_users")