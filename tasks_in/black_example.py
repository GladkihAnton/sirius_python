# pip install black
# black task_in/black_example.py

s = "anagramo"
t = "nagaramd"
dict1={}
dict2={}
for index in range(len(s)):
    if s[index] not in dict1:
        dict1[s[index]]=1
    else:
        dict1[s[index]]+=1

for index in range(len(t)):
    if t[index] not in dict2:
        dict2[t[index]]=1
    else:
        dict2[t[index]]+=1
