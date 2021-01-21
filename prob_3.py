def contador_pares(ar,k): 
    ''' Usando um metodo de hashing, com uma lista de len(k) para armazenar
        o número de ocorrências de cada ar[i]%K, e calcular o número de pares depois,
        para não ter que usar nested for loops.
    '''
    # Cria uma lista de ocorrências
    ocorrencias = [0] * k
    pares_divisiveis = 0
    # Contando todas as ocorrências
    for i in range(len(ar)): 
        ocorrencias[ar[i] % k]+= 1
          
    # Contando os pares se os dois números forem divisiveis por k
    # números com % 0
    pares_divisiveis = ocorrencias[0] * (ocorrencias[0]-1)/2
      
    # Contando todos os pares possíveis com % entre 1 e k-1
    i = 1
    while(i <= k//2 and i!=(k- i)): 
        pares_divisiveis += ocorrencias[i] * ocorrencias[k-i] 
        i+= 1
  
    # Se k for par, contar números com %K//2
    # Que não teriam sido contados no while loop
    if( k% 2 == 0 ): 
        pares_divisiveis += (ocorrencias[k//2] * (ocorrencias[k//2]-1)/2)
      
    # int() para retornar o número inteiro, e não um float de final .0 por conta das divisões
    return int(pares_divisiveis)

ar = [1, 2, 3, 4, 5, 6]
k = 5
print(contador_pares(ar, k))

ar = [1, 3, 2, 6, 1, 2]
k= 3
print(contador_pares(ar, k)) 