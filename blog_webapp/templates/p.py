loop_list = []
for i in range(200):
   if i%100 == 0:
     i += 1
     continue
   loop_list.append(i)
   i += 1
print(loop_list)