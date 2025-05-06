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
result1=v_int+1
print('Resault1: '+ str(result1)) # addition

result2=v_int-1
print('Resault2: '+ str(result2)) # subtraction

result3=v_int*1
print('Resault3: '+ str(result3)) # multiplication

result4=v_int/2
print('Resault4: '+ str(result4)) # division

result5=v_int % 2 
print('Resault5: '+ str(result5)) # remainder after division by 2

result6 = int(1.337) 
print('Resault6: '+ str(result6)) # explicit type conversion

result7_list1 = [1,4,8]
result7_list1.append(8)
result7_list2 = [1,3,3,7]
result7_list1.insert(4,result7_list2)
result7=result7_list1+result7_list2
print('Resault7: '+ str(result7)) # - create a variable, put some values ​​in it, add more values ​​there using the .append() function, add one list inside another, add 2 different lists