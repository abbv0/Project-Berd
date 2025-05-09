#3 HW
# Write a loop over a list
for one_element in [1, 2, 3, 4, 5, 6, 7, 8]: print(one_element) 

# Write a loop over a list of strings. Output values ​​if the element's string length is > 5 characters.
for one_element in ['hell', 'hello, World!', 'yes', 'holy shmoly']: 
    if len(one_element)<=5: print(one_element)

# Write a cycle on a list with lists. Inside the cycle on the outer sheet - make a cycle on the inner lists. Output the elements.
l = [['1.1','1.2','1.3'], ['2.1','2.2','2.3']]
for main_list_element in l: 
    for inner_list_element in main_list_element: 
        print(inner_list_element) 

# Write a loop over a dictionary (over dictionary keys). Output keys and output values.
d = {'first': 1, 'Second': 2, 'holy': 'shmoly'}
for key in d.keys():
    print(key,': ',d.get(key)) 

# Print numbers from 1 to 10000 using while loop and break
i=0
while True: 
    i+=1 
    print(i)
    if i == 10000: 
        break 

# Create 2 dictionaries with different keys. Make a 3rd dictionary - so that it contains values ​​from both the 1st and the second dictionary - using a loop through the second dictionary.
d1 = {'One': 1, 'Two':2, 'Holy': 'shmoly'}
d2 = {'Rich': 'Moscow', 'Saint': 'Petersburg'}
for key in d2.keys():
    d1[key] = d2.get(key)
print(d1)

#3 lessons loops
l1 = [1, 2, 3, 4, 5, 6, 7, 8]
v_sum = 0
for one_element in l1:
    if one_element % 2 == 0:
        v_sum += one_element
print(v_sum)
l2 = [100, 200, 1]
v_sum = 0
for one_element in l2:
    v_sum = v_sum + one_element
print(v_sum)
# for one in l2:
#     print(one)
#     print(one * 10)
d1 = {
    'one': 123,
    'two': 456
}
# for one_key in d1.keys():
#     print(one_key, d1.get(one_key))
i = 0
d2 = dict()
print(d2)
for one_element in l1:
    d2[i] = one_element
    i = i + 1
print(d2)
i = 0
import time
# for one_element in [1, 2, 3]:
#     for i in [1, 2, 3, 4, 5]:
#         print(f'one element = {str(one_element)}')
#         print('hello!', i)
#         i += 1 #i = i + 1
#         time.sleep(1)
i = 0
while True:
    print('hello!', i)
    i += 1
    if i > 100:
        break

