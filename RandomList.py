from random import randint
list = []
for i in range(randint(10,20)):
  list.append(randint(1,50))
list[0] = min(list)

print(list)
    
  

