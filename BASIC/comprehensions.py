#list comprehensions: using []
ls=[i for i in range(100) if i%3==0]# in one line list of all numbers divisible by 3
print(ls)
#comp.dictionary: using{key:value}
#dict1={0:'item0',1:'item1',.............}
dict1={ i:f"item {i}" for i in range(10) if i%2==0}
print(dict1)
#for reversing the key and values in dictionary
dict1={value:key for key,value in dict1.items()}
print(dict1)

#comprehension set: using {}(like comp. list but they return unique values)
set1={i for i in [1,2,1,5,35,25,2,35]}
print(set1)
#comp. generators: using ()
gen1=(i for i in range(10) if i%2==0) 
print(gen1)