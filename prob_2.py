def diagonal_dif(matrix):
    diagonal_esquerda = 0
    diagonal_direita = 0
    
    for i in range(len(matrix)):
        #Pegando o primeiro número da primeira matrix, depois o segundo da segunda e assim vai.
        diagonal_esquerda += matrix[i][i]
    
    for i,row in enumerate(matrix):
        #Como o i começa como 0, é preciso colocar -1 para o funcionamento do indexing negativo
        diagonal_direita += row[-i-1]
    
    return abs(diagonal_esquerda - diagonal_direita)

print(diagonal_dif([[1,2,3],
                    [4,5,6],
                    [9,8,9]]))