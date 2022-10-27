import random

num1 = random.randint(0,5)

#lists

sched = ["CMSC 140", "I-E 100", "CMSC 510"]
#print(sched[0])
sched[0] = "Advanced Sleeping"
#print(sched[0])

random_num = []
for i in range(20):
    random_num.append(random.randint(1,100))
    
print(random_num)

for i in range(20):
    random_num[i] = random_num[i]**(1/2)
print (random_num)

new_list = [0] * 20
print(new_list)