#建立一個計算機

num1 = float(input("請輸入第一數: "))
op = input("請輸入運算符號: ")
num2 = float(input("請輸入第二數: "))


if op == "+":
    ans = num1+num2 
elif op == "-":
    ans = num1 - num2
elif op == "*":
    ans = num1 * num2 
elif op =="/":
    ans = num1 / num2 

print(ans)

