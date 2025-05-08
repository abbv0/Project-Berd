#1 HW
# addition
v_int = int(3.333)
result1=v_int+1
print('Result1: '+ str(result1)) 

# subtraction
result2=v_int-1
print('Result2: '+ str(result2)) 

# multiplication
result3=v_int*1
print('Result3: '+ str(result3)) 

# division
result4=v_int/2
print('Result4: '+ str(result4)) 

# remainder after division by 2
result5=v_int % 2 
print('Result5: '+ str(result5)) 

# explicit type conversion
result6 = int(1.337) 
print('Result6: '+ str(result6)) 

# - create a variable, put some values ​​in it, add more values ​​there using the .append() function, add one list inside another, add 2 different lists
result7_list1 = [1,4,8]
result7_list1.append(8)
result7_list2 = [1,3,3,7]
result7_list1.insert(4,result7_list2)
result7=result7_list1+result7_list2
print('Result7: '+ str(result7)) 

#1 lessons variables 
v_float = 1.1
v_String = 'test spring'
v_list = list()
v_list = [1,'abc',3,4,5]
v_list2 = [1,v_list]
print(v_int)
print(v_float)
print(v_String)
print(v_list)
print(v_list2)