from collections import Counter, deque
from queue import Queue


Input= "hello"

resultStr = ''
result = " ".join(list(map(lambda x : resultStr + x, Input[::-1])))

Inputstr =  "PYTHON"
count_v = 0
result1 = list(map(lambda x : count_v +1 if x in ('a', 'e', 'i', 'o', 'u') else 0, Inputstr.lower()))
# print(sum(result1))

Input4= "swiss"

for i in range(len(Input4)):
    print(Input4[i] , Input4[i+1:])
    if Input4[i] in Input4[i+1:]:
        print(Input4[i])
        break

## anagrams
s1, s2 = "listen", "silent"
print(sorted(s1) == sorted(s2))

Input56 =  "banana"

print(Counter(Input56))

s="banana"
sub="an"

count = 0
i,j = 0, 0

while (i<len(s)):
    while(j < len(sub)):
        if s[i] == sub[j]:
            count = count +1
            j=j+1
        else:
            i = i+1
    i = i+1    
              
    
print("hello world".capitalize())



double_ended_stack = deque()

double_ended_stack.append("a")
double_ended_stack.append("b")
double_ended_stack.append("c")

print(double_ended_stack)

left = double_ended_stack.popleft()
print(left)

right = double_ended_stack.pop()
print(right)

Inputp= "(()(()("

stack = []


mapping_dict = {")": "("}

for i in range(len(Inputp)):
    if Inputp[i] in "({[":
        stack.append(Inputp[i])
    elif  Inputp[i] in ")}]":
        if stack:
            top = stack.pop()
            if mapping_dict[Inputp[i]] != top:
                print(f"error at {i}")  

else:
    print(f"errr at {stack[-1]}")



Inputr= [1,2,2,3,1]

seen = set()
resultd = []
for num in Inputr:
    if num not in seen:
        resultd.append(num)
        seen.add(num)
print(resultd)


Input1 =  [1,3,5]
Input2 = [2,4,6]

Input1.extend(Input2)
print(Input1)

Input1 =  [1,3,5]
Input2 = [3,4,6]
merged = []
i, j  = 0, 0
while(i < len(Input1) and j < len(Input2)):
    if Input1[i]< Input2[j]:
        merged.append(Input1[i])
        i = i+1
    else:
        merged.append(Input2[j])
        j+=1    
merged.extend(Input1[i:])
merged.extend(Input2[j:])

print(merged)

Input= [1,2,3,4,5]
k=2

n = len(Input)
k %= n

rorated = Input[-k:] + Input[:-k]
print(rorated)


