#set and dict

"""s = {i**2 for i in range(1,5)}
print(s)""" 


"""ls = [1,2,3,4]
s = {i**2 for i in ls}
print(ls)""" 


"""ls = [1,2,3,4]
s = list({i**2 for i in range(1,6)})
print(s)""" 


"""ls = [1,2,'1','2',-5,6,5]
s = {int(i) for i in ls}
print(s)"""  

"""import time

start = time.time()
s = [i**2 for i in range(1000000)]
finish = time.time()
print(finish - start) 

start_for = time.time()
ls = []
for n in range(1000000) :
    ls.append(n**2)
finish_for = time.time()
print(finish_for - start_for)""" 


"""di = {
    'nino' : 2,
    'dato' : 3,
    'vato' : 4,
    'kato' : 5
}

#dict_transf = {x:y for x,y in di}

dict_transf = {key.upper() : value for key,value in di.items()}

print(dict_transf)""" 

"""di = {
    'nino' : 2,
    'dato' : 3,
    'vato' : 4,
    'kato' : 5
}

ls = [['ch',1], ['uk',2], ['geo',3], ['alb',4]]

#dict_transf = {x:y for x,y in di}

dict_transf = {key.upper() : value for key,value in ls}

print(dict_transf)""" 

"""di = {
    'nino' : 2,
    'dato' : 3,
    'vato' : 4,
    'kato' : 5
}

ls = [['ch',1,'A'], ['uk',2,'playoff-A'], ['geo',3,'playoff-B'], ['alb',4,'C']]

#dict_transf = {x:y for x,y in di}

dict_transf = {key.upper() : (value,place) for key,value,place in ls}

print(dict_transf)""" 

"""ls = [10,11,12,13]

ite = iter(ls)

print(next(ite)) 
print(next(ite))
print(next(ite))    
print(next(ite))""" 

"""ls = [10,11,12,13]

gen = (x**2 for x in ls)

print(next(gen))""" 

"""ls = [10,11,12,13]

gen = [x**2 for x in ls]

print(gen)""" 


"""
#ls = list(range(10000000))

ls = (x for x in range(10000000))

for i in ls:
    if i > 50:
        break
    print(i, end="")
    
 
print(ls)""" 
