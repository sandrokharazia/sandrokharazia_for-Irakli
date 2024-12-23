# list comrehersions

"""n = 6

result_list = [0]*6
for i in range(1,n+1) :
    result_list[i-1] = i**2
    
result_list = [i**2 for i in range(1,n+1)]

print(result_list)""" 



"""n = 5
result_list = [1 for _ in range(n)]

print(result_list)""" 



"""list_number = [12,13,46,18,43]
result_list =  [i/3 == 0 for i in list_number]
    
print(result_list)""" 



"""list_number = [12,13,46,18,43]
result_list =  [i for i in list_number]
    
print(result_list)""" 



"""list_number = [12,13,46,18,43]
result_list =  [i**2 for i in list_number]
    
print(result_list)""" 



"""list_number = [12,13,46,18,43]
result_list =  [i**2 for i in list_number if i/3 == 0]
    
print(result_list)""" 



"""list_number = [12,13,46,18,43]
result_list =  [i**2 for i in list_number if i%3 == 0]
    
print(result_list)""" 



"""list_number = [12,13,46,18,43]
result_list =  [2*i-3 for i in list_number if i%3 == 0]
    
print(result_list)""" 



"""print('python'.split('t'))"""  
"""print('p y t h o n'.split(' '))"""  

"""numb = input('input your numbers with spaces: ')

print(numb)""" 
               


"""numb = input('input your numbers with spaces: ')
result_list = [i for i in numb.split(' ')]

print(result_list)""" 
                      
                      
                      
"""numb = input('input your numbers with spaces: ')
result_list = [int(i) for i in numb.split(' ')]

print(result_list) """ 
                       
                       
"""text = 'python'
result = [el.upper() for el in text]

print(result) """ 



"""result = [i for i in range(100,200) if i%2 != 0 and i%3 != 0]   

print(result)   """ 




"""names = ['ia', 'mzia', 'enzela', 'lamara', 'tamara', 'gogucha', 'efrosine']
result = [n for n in names if len(n)>4]  

print(result)""" 




"""names = ['ia', 'mzia', 'enzela', 'lamara', 'tamara', 'gogucha', 'efrosine']
result = [n.capitalize() for n in names if len(n)>4]  

print(result)""" 



"""names = ['IA', 'MZIA', 'ENZELA', 'LAMARA', 'TAMARA', 'GOGUCHA', 'EFROSINE']
result = [n.capitalize() for n in names if len(n)>4]  

print(result)"""



"""names = ['ia', 'mzia', 'enzela', 'lamara', 'tamara', 'gogucha', 'efrosine']
result = [ord(n[0]) for n in names if len(n)>4]  

print(result)""" 


"""numb = [12,13,26,87,101,13,57]
result = ['even' if x%2 == 0 else 'odd' for x in numb]

print(result) """



"""numb = [12,13,26,87,101,13,57]
result = [f'{x} is even' if x%2 == 0 else f'{x} is odd' for x in numb]

print(result)"""



"""list_1 = [1,2,3]
list_2 = [11,12,13]

result = []

for i in list_1 :
    for j in list_2 :
        result.append((i,j))

print(result)""" 



"""list_1 = [1,2,3]
list_2 = [11,12,13]

result = [(i,j)
          for i in list_1
          for j in list_2
           ]

print(result)""" 



"""list_1 = [1,2,3]
list_2 = [11,12,13]

result = [(i,j)
          for i in list_1 if i%3 == 0 
          for j in list_2 if j%3 == 0 
          ]

print(result)""" 



"""list_1 = [1,2,3]
list_2 = [11,12,13]

result = [[f"{i}*{j} = {i*j}"]
          for i in list_1 if i%3 == 0 
          for j in list_2 if j%3 == 0 
          ]

print(result)""" 



"""list_1 = [1,2,3]
list_2 = [11,12,13]

result = [[f"{i}*{j} = {i*j}"]
          for i in range(1,11) 
          for j in range(1,11)
          ]

print(result)""" 



"""matrix = [[1,2],[3,4,5],[5,6,7,8]]
result = [elem
          for comb_elem in matrix
          for elem in comb_elem
           ]

print(result)""" 



"""A = [[1,2,3],[4,5,6],[7,8,9]]
result = [[x**2 for x in comb_elem] for comb_elem in A]

print(result)""" 




"""result = [x**2 for x in[i+10 for i in range(5)]]

print(result)""" 