# Write a function that receives a list as input, bubble sorts it, and then returns the sorted list.
# list1 = [1,9,2,7,3,5,6,4,8]

# def func_bubble_sort(list):
#     v_lenght_list = len(list)
#     i=0
#     for element in list:
#         i+=1
#         if element>list[i]:
#             v_lenght_list -= v_lenght_list
#             temp_element = list[i]
#             list[i] = element
#             element = temp_element
#         #if v_lenght_list==0: 
#         #    break
#     print(f'!i :{i}')
#     return(list)

# print(func_bubble_sort([1,9,2,7,3,5,6,4,8]))
    
        
def func_bubble_sort(l1):
    v_lenght_list = len(l1)
    i=0
    temp_element = 0
    v_iteration = v_lenght_list
    for element in l1:
        i+=1
        i = i%v_lenght_list
        if element>l1[i]:
            temp_element = l1[i]
            l1[i] = l1[i-1]
            l1[i-1] = temp_element
            v_iteration-=1
        if v_iteration==0: 
            break
        print(f'i: {i}, l1: {l1}, temp_element: {temp_element},l1[i]: {l1[i]}, element: {element}, v_iteration: {v_iteration}')
    return(l1)
print(func_bubble_sort([1,9,2,7,3,5,6,4,8]))
#######№№3

