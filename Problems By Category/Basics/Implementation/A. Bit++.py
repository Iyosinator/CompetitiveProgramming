n = int(input())
count = 0

for i in range(n):
    operation = input()
    if operation  == "++X" or operation =="X++":
        count +=1
    elif operation  == "--X" or operation == "X--":
        count -=1
print(count)
