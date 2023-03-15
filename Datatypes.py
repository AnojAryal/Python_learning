#data types in python


num=5
print(type(num))

b=5.5
print(type(b))

c=5+6j
print(type(c))


e=5.7
print(e)
f=int(e)
print(f)
print(type(f))

k=8
print(float(k))

c=complex(num,f)
print(c)

#in case with bool it simply means true and false

d=k<f
print(d)
print(type(d))

ram=10
shyam=15
print(ram)
print(shyam)
hari=ram<shyam
print("10 is less than 15")
print(hari)
print(type(hari))

lst=[22,45,67,77,89]
print(lst)
print(type(lst))

s={1,2,3,4,5}
print(s)
print(type(s))

tup=(4,5,8,9,12)
print(tup)
print(type(tup))

s="franzy"
print(s)
print(type(s))

i=(10)
print(range(i))
print(list(range(i)))

#dictonary

dict= {'anoj':'iphone','baibhav':'oneplus','santosh':'samsung'}
print(dict)
print(dict.keys())
print(dict.values())

print(dict['anoj'])
print(dict.get('baibhav'))

#in dictonary values can be same but key must be different
#anoj is the key where iphone is the values
