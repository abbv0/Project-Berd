#3 conditional
a = 5
a = 3
if (a > 2) and ((1==1) or (1!=2)):
    print('a > 2')
    print('hello')
    if a > 10:
        print('a > 10')
elif a == 2:
    print('a = 2')
elif a == 1:
    print('a = 1')
else:
    print('a < 2')
l1 = [1, 2, 3]
if a in l1:
    print('a inside l1')
if False:
    print('a elements in l1')

#3 HW
v_1=1
v_2=32.3
v_3=4.66
if v_1>v_2 and v_1>v_3: 
    print('Result1: 1 BIG')
elif v_1<v_2 and v_2>v_3:
    print('Result1: 2 BIG')
elif v_1<v_3 and v_2<v_3:
    print('Result1: 3 BIG')
else: 
    print('Result1: there is equality') # Use conditional operator - compare several numbers and print.
v_1 = 5
print('Result2: ',v_1 / 10 if v_1 >= 0 else v_1 * 10) # If the number in the variable is positive, multiply it by 10, and if it is negative, divide it.

v_1 = 4
print ('Result3: ',v_1/2 if v_1%2>0 else v_1*3) # If the number is a multiple of 2m, then divide it by 2 and output it - otherwise, multiply by 3

v_1 = 4
print ('Result4: ',v_1/2 if v_1>=10 else v_1*2 if v_1%2>0 else v_1*3) # Multiply even by 3, multiply odd by 2 if less than 10 and divide by 10 if less

v_1=4 
v_2=2.2
print('Result5: ',v_1+v_2 if (type(v_1) == int and type(v_2) == int) else 'One of the variables is not int') # If each variable is of type int - output their sum

l_1 = [1, 2, 4, 'Hello, world!', 228.322]
print('Result6: ','3 found' if 3 in l_1 else '3 not found' ) # use the if statement with the list type to check if the value is in the list.
