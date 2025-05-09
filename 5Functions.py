#5 HW
# Write a function with 3 parameters - and set the last parameter to a default value.
def func_name_return(Firstname, Lastname, Surname='Surname doesnt exist'):
    return(f'My name is {Firstname}, {Surname}, {Lastname}!')
print(func_name_return(Firstname='Andrew', Lastname='Pivovarchuk'))

# Call a function with 1 parameter inside a loop.
def func_city_print(name):
    print(f'City is :{name}')
for i in [1,2,3]: 
    func_city_print(name='Saint Petersburg')

# Write a function with 1 parameter - and pass a variable of type list to this parameter. The function should return the sum of all the elements of list that were passed to it. Return via return
list_for_sum = [1,2,3]
def func_sum_list(list):
    for element in list: 
        element+=element
    return element
print(func_sum_list(list_for_sum))

# Call one function inside another.
def func_name_choice():
    print('You choose name')
def func_name_call(choice):
    if choice == 'name': 
        return func_name_choice() 
    else: 
        print('You choose something else') 
func_name_call(choice =' name')

# Write a function that receives a list as input, bubble sorts it, and then returns the sorted list.


#5 Functions
def func1():
    print('a')
    print('b')
# for one_element in [1, 2, 3]:
#     func1()
def func2(local_element):
    print(local_element, local_element * 2)
# for one_element in [1, 2, 3, 'hello!']:
#     func2(local_element=one_element)
def func3(name, surname='Сидоров', otchestvo='petrovich'):
    print(f'name is {str(name)}, surname is {str(surname)}, {otchestvo}')
func3(name='Иван', surname='Петров')
func3('Иван', 'Петров')
func3(name='Иван')
def sum2(a, b):
    result = a + b
    return result
def sum3(c):
    return sum2(c, c)
print(sum3(100))
# print(sum2(a=1, b=5))
def any_function(a, b):
    result1 = a + b
    result2 = a - b
    return result1, result2
var1, var2 = any_function(10, 8)
# print(var1)
# print(var2)
def func123(a: float):
    return a + 2
# def func123(a: str):
#     return a
print(func123(1))
def loop1():
    for element in [1, 2, 3, 4, 5, 6, 7, 8]:
        print(element)
        if element > 3:
            return None
loop1()
