MY_LIST=[1,24,6,1,8,6,24,24,6]  #notre lise
print(MY_LIST.count(1))
print(MY_LIST.count(24))	
print(MY_LIST.count(6))
print(MY_LIST.count(8))
my_dict={1:MY_LIST.count(1),24:MY_LIST.count(24),6:MY_LIST.count(6),8:MY_LIST.count(8) }# on utlisi MY_LIST.count pour compter l'occurence de chaque élément
print("mon novau dictionnaire est",my_dict)
