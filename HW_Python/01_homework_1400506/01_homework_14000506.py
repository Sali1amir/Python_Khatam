#!/usr/bin/env python
# coding: utf-8

# # 1. Classify each of the following as either a legal or illegal Python identifier:
# 1. fred
# 2. if
# 3. 2x
# 4. -4
# 5. sum_total
# 6. sumTotal
# 7. sum-total
# 8. sum total
# 9. sumtotal
# 10. While
# 11. x2
# 12. Private
# 13. public
# 14. $16
# 15. xTwo
# 16. _static
# 17. _4
# 18. `___`
# 19. 10%
# 20. a27834
# 21. wilma’s

# In[138]:



    fred
    sum_total
    sumTotal
    sumtotal
    Private
    public
    xTwo
    _static
    ___
    a27834


# # 2. What is wrong with the following statement that attempts to assign the value ten to variable x?
# > 10 = x

# In[2]:


x=10; 
print(x)


# # 3. Is "i" a string literal or variable?

# In[13]:


print('“i” is a string literal of length 1')


# # 4. Indicate what each of the following Python statements would print:
# > x = 2
# 1. print("x")
# 2. print(’x’)
# 3. print(x)
# 4. print("x + 1")
# 5. print(’x’ + 1)
# 6. print(x + 1)

# In[151]:


x = 2

print('print("x"):',"x")
print("print('x'):",'x')
print('print(x):',x)
print('print("x + 1"):',"x + 1")
print("print('x' + 1):","Shows Error")
print('print(x + 1):',x + 1)



# # 5. Given the following assignments:
# i1 = 2
# i2 = 5
# i3 = -3
# d1 = 2.0
# d2 = 5.0
# d3 = -0.5;
# # Evaluate each of the following Python expressions.
# 1. i1 + i2
# 2. i1 / i2
# 3. i1 // i2
# 4. i2 / i1
# 5. i2 // i1
# 6. i1 * i3
# 7. d1 + d2
# 8. d1 / d2
# 9. d2 / d1
# 10. d3 * d1
# 11. d1 + i2
# 12. i1 / d2
# 13. d2 / i1
# 14. i2 / d1
# 15. i1/i2*d1
# 16. d1*i1/i2
# 17. d1/d2*i1
# 18. i1*d1/d2
# 19. i2/i1*d1
# 20. d1*i2/i1
# 21. d2/d1*i1
# 22. i1*d2/d1

# In[119]:


i1 = 2; i2 = 5; i3 = -3; d1 = 2.0; d2 = 5.0; d3 = -0.5;
list1 = [i1 + i2,i1 / i2,i1 // i2,i2 / i1,i2 // i1,i1 * i3,d1 + d2,d1 / d2,d2 / d1,d3 * d1,d1 + i2,i1 / d2,d2 / i1,i2 / d1,i1/i2*d1,d1*i1/i2,d1/d2*i1,i1*d1/d2,i2/i1*d1,d1*i2/i1,d2/d1*i1, i1*d2/d1]

for j in range(0,len(list1)):
  print(j+1,'.',list1[j])


#  6. Write the shortest way to express each of the following statements.
# 1. x = x + 1
# 2. x = x / 2
# 3. x = x - 1
# 4. x = x + y
# 5. x = x - (y + 7)
# 6. x = 2*x
# 7. number_of_closed_cases = number_of_closed_cases + 2*ncc

# In[110]:


x=1;y=2;
x+=1
x/=2
x-=1
x+=y
x-=y+7
x*=2
number_of_closed_cases=1;ncc=2; number_of_closed_cases+=2*ncc


# # 7. Is the value -16 interpreted as True or False?

# In[66]:


x=-16
print(bool(x))
print(bool(x<0))
print(bool(x>0))


# # 8. Given the following definitions:
# x, y, z = 3, 5, 7
# evaluate the following Boolean expressions:
# 1. x == 3
# 2. x < y
# 3. x >= y
# 4. x <= y
# 5. x != y - 2
# 6. x < 10
# 7. x >= 0 and x < 10
# 8. x < 0 and x < 10
# 9. x >= 0 and x < 2
# 10. x < 0 or x < 10
# 11. x > 0 or x < 10
# 12. x < 0 or x > 10

# In[84]:


x, y, z = 3, 5, 7
list2 = [ x == 3,x < y,x >= y,x <= y,x != y - 2,x < 10,x >= 0 and x < 10,x < 0 and x < 10,x >= 0 and x < 2,x < 0 or x < 10,x > 0 or x < 10,x < 0 or x > 10]
for i in range(0,len(list2)): print(i+1,'.',bool(list2[i]))


# # 8. Write a Python program that requests an integer value from the user.
# * If the value is between 1 and 100 inclusive, print ”OK;” otherwise, do not print anything.

# In[95]:


x = int(input('Enter an integer number:'))
if x > 1 and 100 > x:
  print("OK")


# # 9. Write a Python program that requests an integer value from the user.
# * If the value is between 1 and 100 inclusive, print ”OK;” otherwise, print ”Out of range.”

# In[96]:


x = int(input('Enter an integer number:'))
if x > 1 and 100 > x:
  print("OK")
else:
  print("Out of range")


# # 10. Write a Python program that:
# * requests five integer values from the user.
# * It then prints the maximum and minimum values entered.
# * If the user enters the values 3, 2, 5, 0, and 1, the program would indicate that 5 is the maximum and 0 is the minimum.
# * Your program should handle ties properly; for example, if the user enters 2, 4 2, 3 and 3, the program should report 2 as the minimum and 4 as maximum.

# In[108]:


list3 = []
counter = 0
while counter < 5:
    number = int(input("Please enter a number: "))
    counter += 1
    list3.append(number)

print(max(list3),'is the maximum and',min(list3),' is the minimum.') 

