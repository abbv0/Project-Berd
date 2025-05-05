#1 variables 
v_int = int(3.333)
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
#1 HW
v_result1=v_int+1
print('Resault1: '+ str(v_result1)) # addition
v_result2=v_int-1
print('Resault2: '+ str(v_result2)) # subtraction
v_result3=v_int*1
print('Resault3: '+ str(v_result3)) # multiplication
v_result4=v_int/2
print('Resault4: '+ str(v_result4)) # division
v_result5=v_int % 2 
print('Resault5: '+ str(v_result5)) # remainder after division by 2
v_result6 = int(1.337) 
print('Resault6: '+ str(v_result6)) # explicit type conversion
v_result7_list1 = [1,4,8]
v_result7_list1.append(8)
v_result7_list2 = [1,3,3,7]
v_result7_list1.insert(4,v_result7_list2)
v_result7=v_result7_list1+v_result7_list2
print('Resault7: '+ str(v_result7)) # - create a variable, put some values ​​in it, add more values ​​there using the .append() function, add one list inside another, add 2 different lists
