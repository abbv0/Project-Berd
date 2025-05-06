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

#HW
v_1=1
v_2=32.3
v_3=4.66
if v_1>v_2 and v_1>v_3: 
    print('Resault1: 1 BIG')
elif v_1<v_2 and v_2>v_3:
    print('Resault1: 2 BIG')
elif v_1<v_3 and v_2<v_3:
    print('Resault1: 3 BIG')
else: 
    print('Resault1: there is equality') # Use conditional operator - compare several numbers and print.
v_1 = 5
print('Resault2: ',v_1 / 10 if v_1 >= 0 else v_1 * 10) # If the number in the variable is positive, multiply it by 10, and if it is negative, divide it.

v_1 = 4
print ('Resault3: ',v_1/2 if v_1%2>0 else v_1*3) # If the number is a multiple of 2m, then divide it by 2 and output it - otherwise, multiply by 3

v_1 = 5
print ('Resault3: ',v_1/2 if v_1>=8 else v_1<8 if v_1%2>0 else v_1*3) # If the number is a multiple of 2m, then divide it by 2 and output it - otherwise, multiply by 3

