a = int(input('how many people is in the whole class?'))
list_score = []
name = []
for i in range (a):
    name_input = input('put ur name')
    score = int(input('pls put in ur score here'))
    name.append(name_input)
    list_score.append(score)
    

highest = 0
for n in range(a):
    if list_score[n]>highest:
        highest = list_score[n]
        high_name = name[n]
print(high_name,'highest:',highest)
lowest = 100

for n in range(a):
    if list_score[n]>lowest:
        lowest = list_score[n]
        low_name = name[n]
print(low_name,"lowest",lowest)
sum_score = sum(list_score)
print("whole class average:",sum_score/a)