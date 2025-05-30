#2 HW
# Create multiple lists. Add them together. In the new dictionary, select only unique values.
l1 = [1,2,322,4,'Hello']
l2 = [3,'4']
l3 = ['three','four']
result1 = {'list1':list(set(l1)),'list2':list(set(l2)),'list3':list(set(l3))}
print('Result1: ',result1)

# Create multiple dictionaries. Dictionaries with base types, dictionaries with sheets, dictionaries with dictionaries.
d_types = {
    'v_int': int(3.333),
    'v_float': 1.1,
    'v_String': 'test spring'
    }
d_lists={'list1':l1,'list2':l2}
d_dicts={'dict_types':d_types,'dict_lists':d_lists}
print('Result2: ', d_dicts) 

# Retrieve values ​​from dictionary via .get()
result3 = d_dicts
result3['dict_types'] = d_types.get('v_int')
print('Result3: ',result3.get('dict_types')) 

# Put one dictionary into another. Then get the values ​​from the nested dictionary
result4 = d_dicts
result4['additional_dict']= {'Morning':'Утро', 'Evening': 'Вечер'}
print('Result4: ',result4.get('additional_dict').get('Evening')) 

# Make a list with dictionary keys. Make a sheet with dictionary meanings.
l_key = [1,2,3,4,'Hello']
l_values = ['one','two','three','four','World!']
Result5 = dict(zip(l_key,l_values))
print('Result5: ',Result5) 

# In an already created dictionary, change the value of an element
Result5[1] = 'first'
print(Result5) 

#2 lessons Collection, dict 
list1 = [1, 2, 3, 'Hello']
print(list1)
print(list1[0])
d1=dict()
d1["first"] = 1
d1["second"] = 12345
print(d1.get("second"))
d2 = {
    'val1':1, 
    'val2':'Hello123',
    1:'test'
    }
print(d2.keys())
print(d2.values()) 
d3 = dict()
d3['new'] = d2
d3['old'] = None
print(d3.get('new').get('val1'))
print(type(d3))
print(d3.items())
