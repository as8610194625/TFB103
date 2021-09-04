#九九乘法表

for i in range(1,10,2):
    for j in range(1,10):
        print(i,"x",j,"=",i*j," ",i+1,"x",j,"=",(i+1)*j)

#剪刀石頭布

import random
punches=["剪刀", "石頭", "布"]
user_1 = input("請出拳(剪刀、石頭、布)")
user_2 = random.choice(punches)
 
while user_1 not in punches:
    print("請出拳(剪刀、石頭、布)")
    user_1 = input()
print("勝負".center(40,"-"))
if (user_1 == "剪刀" and user_2 == "布") or (user_1 == "布" and user_2 == "石頭") or (user_1 == "石頭" and user_2 == "剪刀"):
    print("勝利")
elif user_1 == user_2:
    print("平局")
else:
    print("輸家")