#!/usr/bin/env python
# coding: utf-8

# ## List
# 
# (list = []). 
# 
# You can perform the following commands:
# 
# 1. insert i e: Insert integer  at position .
# 2. print: Print the list.
# 3. remove e: Delete the first occurrence of integer .
# 4. append e: Insert integer  at the end of the list.
# 5. sort: Sort the list.
# 6. pop: Pop the last element from the list.
# 7. reverse: Reverse the list.
# 
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

# In here the first user input will denote the number of operations we will perform with the list. Operations as in given 'insert' , 'print' , 'remove' etc. As we will run the program on a given number of time , hence we will need a for loop for the same.
# 
# Now inside our for loop we will provide one constant variable that will take all operation input within it. Let's call it cmd. Then we will split the input and it will be of string type. 
# 
# The 0th index after splitting will denote the operation such as ' insert ' , 'delete' etc and the '1' , '2' indexes (wherever applicable) will define the user input value and it's new position respectively on the array output.

# In[3]:


lst = []
ui = int(input())
for i in range(ui):
    cmd = input().split()
    if cmd[0]=='insert':
        lst.insert((int(cmd[1])),(int(cmd[2])))
    elif cmd[0]=='print':
        print(lst)
    elif cmd[0]=='remove':
        lst.remove(int(cmd[1]))
    elif cmd[0]=='append':
        lst.append(int(cmd[1]))
    elif cmd[0]=='sort':
        lst.sort()
    elif cmd[0]=='pop':
        lst.pop(int(cmd[1]))
    else:
        lst.reverse()


# ## Hacker Rank accepted solution

# In[ ]:


lst = []
ui = int(input())
for i in range(ui):
    cmd = input().split()
    if cmd[0]=='insert':
        lst.insert(int(cmd[1]),int(cmd[2]))
    elif cmd[0]=='print':
        print(lst)
    elif cmd[0]=='remove':
        lst.remove(int(cmd[1]))
    elif cmd[0]=='append':
        lst.append(int(cmd[1]))
    elif cmd[0]=='sort':
        lst.sort()
    elif cmd[0]=='pop':
        lst.pop()
    elif cmd[0]=='reverse':
        lst.reverse()

