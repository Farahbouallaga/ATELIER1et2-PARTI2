MY_LIST=[12,13,89,90,45 ]
my_dict={"first":12,"second":45}
print(MY_LIST)  
print(my_dict['first'])
print(my_dict['second'])
if my_dict['first' ]==12 or 13 or 89 or 90 or 45:
        MY_LIST1=my_dict['first']
        print(" le 1 er element commun est :",MY_LIST1)
if my_dict['second']==12 or 13 or 89 or 90 or 45:
    MY_LIST2=my_dict['second']
    print("le 2 element commun est :",MY_LIST2)
MY_LIST=[MY_LIST1]+[MY_LIST2]
print("la nouvelle list est :", MY_LIST)
