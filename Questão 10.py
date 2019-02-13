#PERTINÊNCIA
a = {1,2,3,4}
b = {3,4,5,6}
print (1 in a )
print (5 in a )
#CONTINÊNCIA
conjunto1 = {5, 6, 7,'b'} 
conjunto2 = {4, 'a', 9, 5, 6, 7} 

if(conjunto1.issubset(conjunto2)): 
    print('conjunto 1 está contida em lista2') 
else: 
    print('conjunto 1 não está contida em lista2')

#SUBCONJUNTO
a = {1,2,3,4}
c = {1,2}
print(c.issubset(a))
print(a.issubset(c))
    
#IGUALDADE
a = {1,2,3,4}
b = {2,1,3,4}
print(a==b)
