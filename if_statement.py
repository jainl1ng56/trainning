#if 

"""
hungry = True
if hungry:
    print("去吃飯")
"""

"""
rainy = True
if rainy:
    print("rainy day ")
else:
    print("not rainy day")
"""
"""
score = 100
if score == 100:
    print("give 1000")
elif score >=80:
    print("give 500")
elif score >=60:
    print("give 100")
else:
    print("-300")
"""

"""
score = 100
rainy = True
if score ==100 and not(rainy) :
    print(-1000)
else:
    print(300)
"""

def max_num(num1,num2,num3):
    ans = max(num1,num2,num3)
    return ans 

num1 = int(input())
num2 = int(input())
num3 = int(input())

print(max_num(num1,num2,num3))

