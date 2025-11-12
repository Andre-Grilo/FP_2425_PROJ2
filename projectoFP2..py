def cria_posicao(col, lin):
    if type(col) != str or type(lin) != int:                                # Verifica se 'col' é uma string e 'lin' é um inteiro
        raise ValueError("cria_posicao: argumentos invalidos")
    if not (col in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]):     # Verifica se 'col' é uma das letras permitidas (de "a" a "j")
        raise ValueError("cria_posicao: argumentos invalidos")
    if not (lin <= 10 and lin >= 1):                                        # Verifica se 'lin' está entre 1 e 10
        raise ValueError("cria_posicao: argumentos invalidos")
    return (col, lin)

def obtem_pos_col(p):
    return p[0]             # Retorna a primeira parte da posição "p", que representa a coluna

def obtem_pos_lin(p):
    if 1 <= p[1] and 9 >= p[1]:             # Verifica se o valor da linha está entre 1 e 9
        return p[1]                         # Retorna a linha se estiver entre 1 e 9
    else:
        a = str(p[1])                       # Converte o valor da linha para uma string, caso tenha mais de um dígito
        return int(a[0])*10+int(a[1])       # Retorna os dígitos da string e os combina para formar o número original

def eh_posicao(p):
    if type(p) == tuple and len(p) == 2:                                                    # Verifica se "p" é um tuplo com 2 elementos
        if obtem_pos_lin(p) <= 10 and obtem_pos_lin(p) >= 1:                                # Verifica se a linha está entre 1 e 10
            if obtem_pos_col(p) in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]:      # Verifica se a coluna está entre as letras permitidas
                return True                                                                 
    return False  

def posicoes_iguais(p1, p2):
    if eh_posicao(p1) and eh_posicao(p2):           # Verifica se ambas as posições, "p1" e "p2", são válidas usando a função "eh_posicao"
        if p1[0] == p2[0] and p1[1] == p2[1]:       # Verifica se tanto a coluna quanto a linha de 'p1' são iguais às de 'p2'
            return True                             # Retorna True se as posições forem iguais


def posicao_para_str(p):
    return str(obtem_pos_col(p)) + str(obtem_pos_lin(p))     # Converte a coluna e a linha em string 

def str_para_posicao(s):
    if len(s) == 2:                                     # Verifica se a string "s" tem 2 caracteres
        return (s[0], int(s[1]))                        # Retorna um tuplo com o primeiro caractere como coluna e o segundo caractere convertido para inteiro como linha
    elif len(s) == 3:                                   # Verifica se a string 's' tem 3 caracteres.
        return (s[0], int(s[1]) * 10 + int(s[2]))       # Retorna um tupl com o primeiro caractere como coluna e os dois últimos como número da linha


#Função alto nível
def eh_posicao_valida(p, n):
    p = (obtem_pos_col(p), obtem_pos_lin(p))                                                # Converte "p" em um tuplo que contém a coluna e linha obtidas da posição
    if eh_posicao(p) and (n >= 2 and n <= 5):                                               # Verifica se "p" é uma posição válida e se "n" está entre 2 e 5
        if n == 2:                                                                          # Para "n" igual a 2, verifica se a coluna está entre "a" e "d" e a linha entre 1 e 4
            if (p[0] in ["a", "b", "c", "d"]) and (p[1] in [1, 2, 3, 4]):
                return True                                                                 
        elif n == 3:                                                                        # Para "n" igual a 3, verifica se a coluna está entre "a" e "f" e a linha entre 1 e 6
            if (p[0] in ["a", "b", "c", "d", "e", "f"]) and (p[1] in [1, 2, 3, 4, 5, 6]):
                return True                                                                 
        elif n == 4:                                                                        # Para "n" igual a 4, verifica se a coluna está entre "a" e "h" e a linha entre 1 e 8
            if (p[0] in ["a", "b", "c", "d", "e", "f", "g", "h"]) and (p[1] in [1, 2, 3, 4, 5, 6, 7, 8]):
                return True                                                                 
        elif n == 5:                                                                        # Para "n" igual a 5, verifica se a coluna está entre "a" e "j" e a linha entre 1 e 10
            if (p[0] in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]) and (p[1] in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
                return True                                                                 
    return False                                                                            


#função alto nivel
def obtem_posicoes_adjacentes(p, n, d):
        
    colunas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]            # Lista das colunas válidas
    linhas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]                                # Lista das linhas válidas
    r = ()
    
    #Fica com a posição na lista linhas e na lista colunas
    for i in range(len(linhas)):
        if linhas[i] == obtem_pos_lin(p):
            pos_linha = i
        if colunas[i] == obtem_pos_col(p):
            pos_coluna = i

    if d:    
        if obtem_pos_lin(p) != 1:                                               #Posição acima
            r = r + ((p[0], linhas[pos_linha - 1]), )

        if obtem_pos_lin(p) != 1 and obtem_pos_col(p) != "j":                   #Posição acima à direita
            r = r + ((colunas[pos_coluna + 1], linhas[pos_linha - 1]), )
            
        if obtem_pos_col(p) != "j":                                             #Posição à direita
            r = r + ((colunas[pos_coluna + 1], p[1]), ) 
        
        if obtem_pos_lin(p) != 10 and obtem_pos_col(p) != "j":                  #Posição abaixo à direita
            r = r + ((colunas[pos_coluna + 1], linhas[pos_linha + 1]), )

        if obtem_pos_lin(p) != 10:                                              #Posição abaixo
            r = r + ((p[0], linhas[pos_linha + 1]), )
        
        if obtem_pos_lin(p) != 10 and obtem_pos_col(p) != "a":                  #Posição abaixo à esquerda
            r = r + ((colunas[pos_coluna - 1], linhas[pos_linha + 1]), )

        if obtem_pos_col(p) != "a":                                             #Posição à esquerda
            r = r + ((colunas[pos_coluna - 1], p[1]), ) 

        if obtem_pos_lin(p) != 1 and obtem_pos_col(p) != "a":                   #Posição acima à esquerda
            r = r + ((colunas[pos_coluna - 1], linhas[pos_linha - 1]), ) 

        return tuple(filter(lambda x : eh_posicao_valida(x, n) , r ))           #Retorna um tuplo das posições adjacentes válidas

    else:
        if obtem_pos_lin(p) != 1:                                               #Posição acima
            r = r + ((p[0], linhas[pos_linha - 1]), )
        
        if obtem_pos_col(p) != "j":                                             #Posição à direita
            r = r + ((colunas[pos_coluna + 1], p[1]), ) 
        
        if obtem_pos_lin(p) != 10:                                              #Posição abaixo
            r = r + ((p[0], linhas[pos_linha + 1]), )

        if obtem_pos_col(p) != "a":                                             #Posição à esquerda
            r = r + ((colunas[pos_coluna - 1], p[1]), ) 
        
        return list(filter(lambda x : eh_posicao_valida(x, n) , r ))            #Retorna uma lista das posições adjacentes válidas

#função extra 1
def obtem_dimensoes(n):
    if n == 2:          #Se "n" for igual a 2, retorna 4
        return 4    
    elif n == 3:        #Se "n" for igual a 3, retorna 6
        return 6
    elif n == 4:        #Se "n" for igual a 4, retorna 8
        return 8
    elif n == 5:        #Se "n" for igual a 5, retorna 10
        return 10

#função extra 2
def tab_pos_tuplo(n):
    colunas = ()
    tab = ()
    m = obtem_dimensoes(n)
    for i in range(m):                                       #Itera sobre a quantidade de colunas
        colunas = colunas + ((chr(ord('a') + i)), )          #Adiciona a coluna correspondente (letras de "a" a "j") ao tuplo de colunas

    linhas = tuple(range(1, m + 1))                          #Cria um tuplo de linhas que vai de 1 até "m"

    for i in linhas:                                        #Itera sobre cada linha
        for x in colunas:                                   #Itera sobre cada coluna
            tab = tab + ((x, i), )                          #Adiciona a posição (coluna, linha) ao tuplo de posições
    return tab

#função alto nivel
def ordena_posicoes(t, n):
    if t == ():
        return ()
    m = obtem_dimensoes(n)
    colunas = ()
    tab = ()
    tab_prov = ()
    r = ()
    tab = tab_pos_tuplo(n)
    for i in range(m):
        colunas = colunas + ((chr(ord('a') + i)), )         # Adiciona as colunas correspondentes (letras de "a" a "j")
    
    linhas = tuple(range(1, m + 1))                         # Cria um tuplo de linhas que vai de 1 até "m"
    
    #Determinar as 4 posições do meio
    meio = m // 2
    pos_centrais = ((colunas[meio-1], linhas[meio-1]),(colunas[meio], linhas[meio-1]), (colunas[meio-1], linhas[meio]), (colunas[meio], linhas[meio]))
    
    if n == 2: 
        #Guardar as outras posições todas sem ser as centrais
        for i in tab:                                   #Itera sobre todas as posições no tabuleiro
            if i not in pos_centrais:                   #Se a posição não é central
                tab_prov = tab_prov + (i, )             #Adiciona a posição ao tuplo provisório

        tab_ordenado = pos_centrais + tab_prov          #Combina as posições centrais com as restantes

        #Ver quais as posiçoes que nos interessam
        for i in tab_ordenado:                          #Itera sobre as posições ordenadas
            if i in t:                                  # Se a posição está em "t"
                r = r + (i, )                           #Adiciona a posição ao resultado
        return r
    
    #Define as posições ordenadas manualmente
    elif n == 3:
        
        tab_ordenado = (('c', 3), ('d', 3), ('c', 4), ('d', 4), ('b', 2), ('c', 2), ('d', 2), ('e', 2), ('b', 3), ('e', 3), ('b', 4), ('e', 4), ('b', 5), ('c', 5), ('d', 5), ('e', 5), ('a', 1), ('b', 1), ('c', 1), ('d', 1), ('e', 1), ('f', 1), ('a', 2), ('f', 2), ('a', 3), ('f', 3), ('a', 4), ('f', 4), ('a', 5), ('f', 5), ('a', 6), ('b', 6), ('c', 6), ('d', 6), ('e', 6), ('f', 6))
        for i in tab_ordenado:                          #Itera sobre as posições ordenadas
            if i in t:                                  #Se a posição está em "t"
                r = r + (i, )                           #Adiciona a posição ao resultado
        return r                                        
    elif n == 4:
        tab_ordenado = (('d', 4), ('e', 4), ('d', 5), ('e', 5), ('c', 3), ('d', 3), ('e', 3), ('f', 3), ('c', 4), ('f', 4), ('c', 5), ('f', 5), ('c', 6), ('d', 6), ('e', 6), ('f', 6), ('b', 2), ('c', 2), ('d', 2), ('e', 2), ('f', 2), ('g', 2), ('b', 3), ('g', 3), ('b', 4), ('g', 4), ('b', 5), ('g', 5), ('b', 6), ('g', 6), ('b', 7), ('c', 7), ('d', 7), ('e', 7), ('f', 7), ('g', 7), ('a', 1), ('b', 1), ('c', 1), ('d', 1), ('e', 1), ('f', 1), ('g', 1), ('h', 1), ('a', 2), ('h', 2), ('a', 3), ('h', 3), ('a', 4), ('h', 4), ('a', 5), ('h', 5), ('a', 6), ('h', 6), ('a', 7), ('h', 7), ('a', 8), ('b', 8), ('c', 8), ('d', 8), ('e', 8), ('f', 8), ('g', 8), ('h', 8))
        for i in tab_ordenado:                          #Itera sobre as posições ordenadas
            if i in t:                                  #Se a posição está em "t"
                r = r + (i, )                           #Adiciona a posição ao resultado
        return r
    elif n == 5:
        tab_ordenado = (('e', 5), ('f', 5), ('e', 6), ('f', 6), ('d', 4), ('e', 4), ('f', 4), ('g', 4), ('d', 5), ('g', 5), ('d', 6), ('g', 6), ('d', 7), ('e', 7), ('f', 7), ('g', 7), ('c', 3), ('d', 3), ('e', 3), ('f', 3), ('g', 3), ('h', 3), ('c', 4), ('h', 4), ('c', 5), ('h', 5), ('c', 6), ('h', 6), ('c', 7), ('h', 7), ('c', 8), ('d', 8), ('e', 8), ('f', 8), ('g', 8), ('h', 8), ('b', 2), ('c', 2), ('d', 2), ('e', 2), ('f', 2), ('g', 2), ('h', 2), ('i', 2), ('b', 3), ('i', 3), ('b', 4), ('i', 4), ('b', 5), ('i', 5), ('b', 6), ('i', 6), ('b', 7), ('i', 7), ('b', 8), ('i', 8), ('b', 9), ('c', 9), ('d', 9), ('e', 9), ('f', 9), ('g', 9), ('h', 9), ('i', 9), ('a', 1), ('b', 1), ('c', 1), ('d', 1), ('e', 1), ('f', 1), ('g', 1), ('h', 1), ('i', 1), ('j', 1), ('a', 2), ('j', 2), ('a', 3), ('j', 3), ('a', 4), ('j', 4), ('a', 5), ('j', 5), ('a', 6), ('j', 6), ('a', 7), ('j', 7), ('a', 8), ('j', 8), ('a', 9), ('j', 9), ('a', 10), ('b', 10), ('c', 10), ('d', 10), ('e', 10), ('f', 10), ('g', 10), ('h', 10), ('i', 10), ('j', 10))
        for i in tab_ordenado:                          #Itera sobre as posições ordenadas
            if i in t:                                  #Se a posição está em "t"
                r = r + (i, )                           #Adiciona a posição ao resultado
        return r


def cria_pedra_branca():        
    return "O"

def cria_pedra_preta():        
    return "X"

def cria_pedra_neutra():       
    return " "

def eh_pedra(p):
    if p in ["O", " ", "X"]:        #Se "p" é uma das pedras válidas
        return True
    return False

def eh_pedra_branca(p):
    if p == cria_pedra_branca():     #Se "p" é uma pedra branca criada pela função
        return True
    return False

def eh_pedra_preta(p):
    if p == cria_pedra_preta():      #Se "p" é uma pedra preta criada pela função
        return True
    return False

def pedras_iguais(p1, p2):
    if eh_pedra(p1) and eh_pedra(p2):
        if p1 == p2:
            return True
    
def pedra_para_str(pedra):
    return pedra

#função alto nivel
def eh_pedra_jogador(p):
    if eh_pedra_branca(p) or eh_pedra_preta(p):
        return True
    return False

#função alto nivel
def pedra_para_int(p):
    if eh_pedra_branca(p):          #Se "p" é uma pedra branca
        return -1
    elif eh_pedra_preta(p):         #Se "p" é uma pedra preta
        return 1
    else:                           #Se "p" não é uma pedra válida
        return 0
    
def cria_tabuleiro_vazio(n):
    if type(n) != int:                                                      #Verifica se "n" é um inteiro
        raise ValueError("cria_tabuleiro_vazio: argumento invalido")
    if n < 2 or n > 5:                                                      #Verifica se "n" está dentro dos limites 
        raise ValueError("cria_tabuleiro_vazio: argumento invalido")
    
    tab_t = tab_pos_tuplo(n)
    tab = {}
    for i in tab_t:                                                         #Para cada posição no tabuleiro
        coloca_pedra(tab, i ,cria_pedra_neutra())                           #Coloca uma pedra neutra na posição

    return tab 

def cria_tabuleiro(n, tp, tb):
    if not( type(n) == int and n<=5 and n>=2 and type(tp) == tuple and type(tb) == tuple):          #Verifica se os argumentos são válidos
        raise ValueError("cria_tabuleiro: argumentos invalidos")   
    
    for i in tp:                                                                                    #Para cada posição em "tp"
        if not(eh_posicao(i)):                                                                      #Verifica se a posição é válida
            raise ValueError("cria_tabuleiro: argumentos invalidos") 
        if not(eh_posicao_valida(i, n)):                                                            #Verifica se a posição é válida para o tamanho do tabuleiro
            raise ValueError("cria_tabuleiro: argumentos invalidos") 

    for i in tb:                                                                                    #Para cada posição em "tb"
        if not(eh_posicao(i)):                                                                      #Verifica se a posição é válida
            raise ValueError("cria_tabuleiro: argumentos invalidos") 
        if not(eh_posicao_valida(i, n)):                                                            #Verifica se a posição é válida para o tamanho do tabuleiro
            raise ValueError("cria_tabuleiro: argumentos invalidos") 
        
    tab = cria_tabuleiro_vazio(n)                                                                   #Cria um tabuleiro vazio

    for i in tp:                                                                                    #Para cada posição em "tp"
        coloca_pedra(tab, i, cria_pedra_preta())                                                    #Coloca uma pedra preta na posição
    for i in tb:                                                                                    #Para cada posição em 'tb'
        coloca_pedra(tab, i, cria_pedra_branca())                                                   #Coloca uma pedra branca na posição
    return tab

def cria_copia_tabuleiro(t):
    if type(t) == dict:             #Verifica se "t" é um dicionário
        copia = {}
        for i in t:
            copia[i] = t[i]         #Copia  o valor
        return copia

    elif type(t) == list:           #Verifica se "t" é uma lista de listas
        copia = []
        for i in t:
            if type(i) == list:
                copia.append(i[:])  #Faz uma cópia com slicing da sublista
            else:
                copia.append(i)     #Copia  o valor
        return copia

def obtem_numero_orbitas(t):
    ultima_chave = list(t)[len(t)-1][1]         #Obtém a última chave do dicionário "t"
    return int(ultima_chave / 2)                #Retorna o número de órbitas como um inteiro

def obtem_pedra(t, p):
    return t[p]

def obtem_linha_horizontal(t, p):
    numero_linha = p[1]
    colunas = ()
    posicoes = ()
    
    m = obtem_dimensoes(obtem_numero_orbitas(t))                                            #Obtém a dimensão do tabuleiro com base no número de órbitas
    for i in range(m):                                                                      #Para cada índice de coluna
        colunas = colunas + ((chr(ord('a') + i)), )                                         #Adiciona a coluna correspondente à tupla de colunas

    for i in colunas:                                                                       #Para cada coluna
        posicoes = posicoes + (((i, numero_linha), obtem_pedra(t, (i,numero_linha))), )     #Adiciona a posição e a pedra à tupla de posições
    
    return posicoes

def obtem_linha_vertical(t, p):
    caracter_coluna = p[0]
    posicoes = ()
    
    m = obtem_dimensoes(obtem_numero_orbitas(t))                                                #Obtém a dimensão do tabuleiro com base no número de órbitas
    linhas = tuple(range(1, m + 1))                                                             #Cria uma tupla com todas as linhas do tabuleiro

    for i in linhas:                                                                            #Para cada linha
        posicoes = posicoes + (((caracter_coluna, i), obtem_pedra(t, (caracter_coluna, i))), )  #Adiciona a posição e a pedra à tupla de posições

    return posicoes    

def obtem_linhas_diagonais(t, p):

    colunas = ()
    cont = -1
    cont1 = 1
    cont2 = 1
    cont3 = 1
    tuplo1 = ()
    tuplo2 = ()


    m = obtem_dimensoes(obtem_numero_orbitas(t))                                    #Obtém a dimensão do tabuleiro com base no número de órbitas
    for i in range(m):                                                              #Preenche o tuplo de colunas
        colunas = colunas + ((chr(ord('a') + i)), )
    
    linhas = tuple(range(1, m + 1))                                                 #Cria um tuplo com todas as linhas do tabuleiro

    for i in range(len(colunas)):                                                   #Para cada coluna
        if colunas[i] == p[0]:                                                      #Encontra o índice da coluna a partir da posição "p"
            indice_colunas = i
    
    indice_linhas = p[1] - 1                                                        #Obtém o índice da linha a partir da posição "p"
    
    while indice_colunas + cont >= 0 and indice_linhas+ cont >= 0:                  #Diagonal superior esquerda
        posicao = (colunas[indice_colunas+cont], linhas[indice_linhas+cont])        #Calcula a posição
        tuplo1 = tuplo1 + ((posicao, obtem_pedra(t, posicao)), )                    #Adiciona a posição e a pedra ao tuplo
        cont = cont - 1 

    tuplo1 = tuplo1 + ((p, obtem_pedra(t, p)), )                                    #Adiciona a posição original

    while indice_colunas + cont1 < m and indice_linhas + cont1 < m:                 #Diagonal inferior direita
        posicao = (colunas[indice_colunas+cont1], linhas[indice_linhas+cont1])      #Calcula a posição
        tuplo1 = tuplo1 + ((posicao, obtem_pedra(t, posicao)), )                    #Adiciona a posição e a pedra ao tuplo
        cont1 = cont1 + 1
    
    while indice_linhas + cont2 < m and indice_colunas - cont2 >= 0:                #Diagonal inferior esquerda
        posicao = (colunas[indice_colunas-cont2], linhas[indice_linhas+cont2])      #Calcula a posição
        tuplo2 = tuplo2 + ((posicao, obtem_pedra(t, posicao)), )                    #Adiciona a posição e a pedra ao tuplo
            
        cont2 = cont2 + 1 

    tuplo2 = tuplo2 + ((p, obtem_pedra(t, p)), )                                    #Adiciona a posição original

    while indice_linhas - cont3 >= 0 and indice_colunas + cont3 < m:                #Diagonal superior direita
        posicao = (colunas[indice_colunas+cont3], linhas[indice_linhas-cont3])      #Calcula a posição
        tuplo2 = tuplo2 + ((posicao, obtem_pedra(t, posicao)), )                    #Adiciona a posição e a pedra ao tuplo
        cont3 = cont3 + 1 

    tuplo1 = tuple(sorted(tuplo1))                                                  #Ordena as posições da primeira diagonal
    tuplo2 = tuple(sorted(tuplo2))                                                  #Ordena as posições da segunda diagonal
    tuplo3 = (tuplo1,tuplo2 )                                                       #Combina as duas tuplas em uma só
    return tuplo3

def obtem_posicoes_pedra(t, j):
    r = ()
    n = obtem_numero_orbitas(t)                                     #Obtém o número de órbitas do tabuleiro
    if type(t) == dict:                                             #Verifica se "t" é um dicionário
        for i in t:                                                 #Itera sobre as chaves do dicionário
            if t[i] == j:                                           #Verifica se a pedra na posição "i" é igual à pedra "j"
                r = r + (i, )
    if type(t) == list:                                             #Verifica se "t" é uma lista
         for i in range(len(t)):                                    #Itera sobre cada linha do tabuleiro
            for x in range(len(t[i])):                              #Itera sobre cada coluna na linha "i"
                if t[i][x] == j:                                    #Verifica se a pedra na posição é igual à pedra 'j'
                    r = r + ((chr(ord('a') + x), i + 1), )
    
    return ordena_posicoes(r, n)

def coloca_pedra(t, p, j):
    t[p] = j
    return t

def remove_pedra(t, p):
    t[p] = cria_pedra_neutra()
    return t

def eh_tabuleiro(t):
    if not(type(t) == dict):                                #Verifica se "t" é um dicionário
        return False
    for i in t:                                             #Itera sobre cada chave do dicionário "t"
        if not (eh_posicao(i) or eh_pedra(t[i])):           # Verifica se a posição "i" é válida e se a pedra na posição "i" é válida
            return False
    return True

def tabuleiros_iguais(t1, t2):
    if eh_tabuleiro(t1) and eh_tabuleiro(t2) and t1 == t2:      #Verifica se ambos os tabuleiros são válidos e se são iguais
        return True

def tabuleiro_para_str(t):
    n = obtem_numero_orbitas(t)
    colunas = ()
    cont = 0
    tab_dividido = ()
    
    m = obtem_dimensoes(obtem_numero_orbitas(t)) 
    for i in range(m):                                                      #Loop para criar as colunas usando letras do alfabeto
        colunas = colunas + ((chr(ord('a') + i)), )                         #Adiciona a letra correspondente à coluna no tuplo

    #Primeira linha
    for i in colunas:                                                       #Itera sobre as colunas para formar a primeira linha do tabuleiro
        if cont == 0:
            r = "    " + str(i) + "   "                                     #Alinha a primeira coluna
        elif cont > 0 and cont < len(colunas) - 1:
            r = r + str(i) + "   "                                          #Adiciona espaços entre as colunas
        elif cont == len(colunas)-1:    
            r = r + str(i) + "\n"                                           #Finaliza a linha com a última coluna e quebra a linha
        cont = cont + 1
    
    linhas = tuple(range(1, m + 1))                                         #Cria um tuplo com números para as linhas do tabuleiro
    
    for i in range(0, len(tab_pos_tuplo(n)), m):                            #Divide o "tab_pos_tuplo" em partes iguais de "m"
            tab_dividido = tab_dividido + (tab_pos_tuplo(n)[i:i+m], )       #Adiciona cada parte ao tuplo "tab_dividido"

    
    for i in linhas:                                                        #Itera sobre os números das linhas para construir cada linha do tabuleiro
        r = r + f"{i:02}" + " "                                             #Formata o número da linha com dois dígitos
        cont1 = 0
        
        for x in tab_dividido[i - 1]:                                       #Itera sobre as pedras na linha atual
            if cont1 == 0:
                r = r + "[" + t[x] + "]"                                    #Adiciona a primeira pedra dentro dos parenteses retos
            else:
                r = r + "-" + "[" + t[x] + "]"                              #Adiciona as demais pedras precedidas por um traço
            cont1 = cont1 + 1

        r += "\n"                                                           #Quebra de linha após a linha de pedras

        if i < m:                                                           #Adiciona os separadores entre as linhas
            r = r + "    "                                                  #Alinha os separadores com as colunas
            for j in range(m):
                if j == 0:
                    r = r + "|"
                else:
                    r = r + "   |"
            r = r + "\n"  # Nova linha após o separador
        
    return r.rstrip()

#função alto nivel
def move_pedra(t, p1, p2):
    a = obtem_pedra(t, p1)          #Obtém a pedra na posição p1
    remove_pedra(t, p1)             #Remove a pedra da posição p1
    coloca_pedra(t, p2 , a)         #Coloca a pedra na nova posição p2
    return t

#função alto nivel
def obtem_posicao_seguinte(t, p, s):
        
        if obtem_numero_orbitas(t) == 2:                        #Verifica se o tabuleiro tem 2 órbitas
            orbita1 = [('a', 1), ('b', 1), ('c', 1), ('d', 1), ('d', 2), ('d', 3), ('d', 4), ('c', 4), ('b', 4), ('a', 4), ('a', 3), ('a', 2)]
            orbita2 = [('b', 2), ('c', 2), ('c', 3), ('b', 3)]
            if p in orbita1:                                    #Verifica se a posição p está na primeira órbita
                orbita = orbita1                                #Se estiver, define orbita como orbita1
            elif p in orbita2:                                  #Verifica se a posição p está na segunda órbita
                orbita = orbita2                                #Se estiver, define orbita como orbita2
            for i in range(len(orbita)):                        #Itera sobre as posições da órbita
                if orbita[i] == p:                              #Encontra o índice da posição p
                    indice_orbita = i                           #Armazena o índice encontrado
            if s:                                               #Verifica se o sentido é para a frente
                r = (indice_orbita + 1) % len(orbita)           #Calcula o índice da próxima posição no sentido horário
            else:
                r = (indice_orbita - 1) % len(orbita)           #Calcula o índice da próxima posição no anti-sentido horário
            return orbita[r]
        
        #Repete o mesmo racicínio para todas as opções de números de orbitas diferentes

        elif obtem_numero_orbitas(t) == 3:
            orbita1 = [('a', 1), ('b', 1), ('c', 1), ('d', 1), ('e', 1), ('f', 1), ('f', 2), ('f', 3), ('f', 4), ('f', 5), ('f', 6), ('e', 6), ('d', 6), ('c', 6), ('b', 6), ('a', 6), ('a', 5), ('a', 4), ('a', 3), ('a', 2)]
            orbita2 = [('b', 2), ('c', 2), ('d', 2), ('e', 2), ('e', 3), ('e', 4), ('e', 5), ('d', 5), ('c', 5), ('b', 5), ('b', 4), ('b', 3)]
            orbita3 = [('c', 3), ('d', 3), ('d', 4), ('c', 4)]
            if p in orbita1:
                orbita = orbita1
            elif p in orbita2:
                orbita = orbita2
            elif p in orbita3:
                orbita = orbita3
            for i in range(len(orbita)):
                if orbita[i] == p:
                    indice_orbita = i 
            if s:
                r = (indice_orbita + 1) % len(orbita)
            else:
                r = (indice_orbita - 1) % len(orbita)
            return orbita[r]

        elif obtem_numero_orbitas(t) == 4:
            orbita1 = [('a', 1), ('b', 1), ('c', 1), ('d', 1), ('e', 1), ('f', 1), ('g', 1), ('h', 1), ('h', 2), ('h', 3), ('h', 4), ('h', 5), ('h', 6), ('h', 7), ('h', 8), ('g', 8), ('f', 8), ('e', 8), ('d', 8), ('c', 8), ('b', 8), ('a', 8), ('a', 7), ('a', 6), ('a', 5), ('a', 4), ('a', 3), ('a', 2)]
            orbita2 = [('b', 2), ('c', 2), ('d', 2), ('e', 2), ('f', 2), ('g', 2), ('g', 3), ('g', 4), ('g', 5), ('g', 6), ('g', 7), ('f', 7), ('e', 7), ('d', 7), ('c', 7), ('b', 7), ('b', 6), ('b', 5), ('b', 4), ('b', 3)]
            orbita3 = [('c', 3), ('d', 3), ('e', 3), ('f', 3), ('f', 4), ('f', 5), ('f', 6), ('e', 6), ('d', 6), ('c', 6), ('c', 5), ('c', 4)]
            orbita4 = [('d', 4), ('e', 4), ('e', 5), ('d', 5)]
            if p in orbita1:
                orbita = orbita1
            elif p in orbita2:
                orbita = orbita2
            elif p in orbita3:
                orbita = orbita3
            elif p in orbita4:
                orbita = orbita4
            for i in range(len(orbita)):
                if orbita[i] == p:
                    indice_orbita = i 
            if s:
                r = (indice_orbita + 1) % len(orbita)
            else:
                r = (indice_orbita - 1) % len(orbita)
            return orbita[r]
        elif obtem_numero_orbitas(t) == 5:
            orbita1 = [('a', 1), ('b', 1), ('c', 1), ('d', 1), ('e', 1), ('f', 1), ('g', 1), ('h', 1), ('i', 1), ('j', 1), ('j', 2), ('j', 3), ('j', 4), ('j', 5), ('j', 6), ('j', 7), ('j', 8), ('j', 9), ('j', 10), ('i', 10), ('h', 10), ('g', 10), ('f', 10), ('e', 10), ('d', 10), ('c', 10), ('b', 10), ('a', 10), ('a', 9), ('a', 8), ('a', 7), ('a', 6), ('a', 5), ('a', 4), ('a', 3), ('a', 2)]
            orbita2 = [('b', 2), ('c', 2), ('d', 2), ('e', 2), ('f', 2), ('g', 2), ('h', 2), ('i', 2), ('i', 3), ('i', 4), ('i', 5), ('i', 6), ('i', 7), ('i', 8), ('i', 9), ('h', 9), ('g', 9), ('f', 9), ('e', 9), ('d', 9), ('c', 9), ('b', 9), ('b', 8), ('b', 7), ('b', 6), ('b', 5), ('b', 4), ('b', 3)]
            orbita3 = [('c', 3), ('d', 3), ('e', 3), ('f', 3), ('g', 3), ('h', 3), ('h', 4), ('h', 5), ('h', 6), ('h', 7), ('h', 8), ('g', 8), ('f', 8), ('e', 8), ('d', 8), ('c', 8), ('c', 7), ('c', 6), ('c', 5), ('c', 4)]
            orbita4 = [('d', 4), ('e', 4), ('f', 4), ('g', 4), ('g', 5), ('g', 6), ('g', 7), ('f', 7), ('e', 7), ('d', 7), ('d', 6), ('d', 5)]
            orbita5 = [('e', 5), ('f', 5), ('f', 6), ('e', 6)]
            if p in orbita1:
                orbita = orbita1
            elif p in orbita2:
                orbita = orbita2
            elif p in orbita3:
                orbita = orbita3
            elif p in orbita4:
                orbita = orbita4
            elif p in orbita5:
                orbita = orbita5
            for i in range(len(orbita)):
                if orbita[i] == p:
                    indice_orbita = i 
            if s:
                r = (indice_orbita + 1) % len(orbita)
            else:
                r = (indice_orbita - 1) % len(orbita)
            return orbita[r]

#função alto nivel
def roda_tabuleiro(t):
    n = obtem_numero_orbitas(t)
    posicoes = tab_pos_tuplo(n)
    tab_prov = {}
    for i in posicoes:                                      #Itera sobre todas as posições do tabuleiro
        n_pos = obtem_posicao_seguinte(t, i, False)         #Obtém a próxima posição no sentido anti-horário
        tab_prov[n_pos] = t[i]                              #Atribui a pedra da posição atual à nova posição no dicionário
    for i in posicoes:                                      #Itera novamente sobre todas as posições do tabuleiro
        if i in tab_prov:                                   #Verifica se a posição atual tem uma nova posição no dicionário
            t[i] = tab_prov[i]                              #Atualiza a posição no tabuleiro com a nova posição da pedra 
    return t

#função alto nivel
def verifica_linha_pedras(t, p, j, k):
    linha = obtem_linha_horizontal(t, p)                                                        #Obtém a linha horizontal correspondente à posição "p"
    coluna = obtem_linha_vertical(t, p)                                                         #Obtém a linha vertical correspondente à posição "p"
    diagonal1 = obtem_linhas_diagonais(t, p)[0]                                                 #Obtém a primeira diagonal correspondente à posição "p"
    diagonal2 = obtem_linhas_diagonais(t, p)[1]                                                 #Obtém a segunda diagonal correspondente à posição "p"
    if not(eh_pedra_branca(obtem_pedra(t, p)) or eh_pedra_preta(obtem_pedra(t, p))):            #Verifica se a pedra na posição "p" é uma pedra válida
        return False
    def contagem_k_presentes(a):
        cont = 0
        for i, z in a:                                                                          #Itera sobre os elementos da sequência
            if z == j:                                                                          #Verifica se o valor atual é igual a j
                cont = cont + 1 
                if cont >= k:                                                                   #Se o contador atingir ou exceder k
                    return True
            else:
                cont = 0  
        return False
    # Verifica se a contagem k de j está presente em alguma das direções (linha, coluna, diagonais)
    return (contagem_k_presentes(linha) or contagem_k_presentes(coluna) or contagem_k_presentes(diagonal1) or contagem_k_presentes(diagonal2))

def eh_vencedor(t, j):
    m = obtem_numero_orbitas(t)                     #Obtém o número de órbitas do tabuleiro
    n = obtem_dimensoes(m)                          #Obtém as dimensões do tabuleiro com base no número de órbitas
    
    for i in tab_pos_tuplo(m):                      #Itera sobre todas as posições do tabuleiro representadas como uma tupla
        if verifica_linha_pedras(t, i, j ,n):       #Verifica se há uma linha de pedras do jogador j com o comprimento n a partir da posição i
            return True
    return False

def eh_fim_jogo(t):
    if eh_vencedor(t, cria_pedra_branca()) or eh_vencedor(t, cria_pedra_preta()):       #Verifica se há um vencedor, seja com pedras brancas ou pretas
        return True
    n = obtem_numero_orbitas(t)                                                         #Obtém o número de órbitas do tabuleiro
    for i in tab_pos_tuplo(n):
        if obtem_pedra(t, i) == cria_pedra_neutra():                                    #Verifica se existe alguma posição com uma pedra neutra
            return False
    return True

def escolhe_movimento_manual(t):
    while True:
        pos_livre = input("Escolha uma posicao livre:")                                      #Pede ao jogador que escolha uma posição livre
        if len(pos_livre) == 2:                                                              #Verifica se a entrada tem dois caracteres
            
            if pos_livre[0] in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"] and pos_livre[1] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                
                a = str_para_posicao(pos_livre)                                             #Converte a string da posição para posição
                
                if eh_posicao(a) and eh_posicao_valida(a, obtem_numero_orbitas(t)):         #Verifica se a posição convertida é válida e se está dentro do número de órbitas
                    if obtem_pedra(t, a) == cria_pedra_neutra():                            #Verifica se a posição escolhida está livre
                        return a
        elif len(pos_livre) == 3:                                                           #Verifica se a entrada tem três caracteres
            
            if pos_livre[0] in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"] and pos_livre[1] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] and pos_livre[2] == "0" :
                
                a = str_para_posicao(pos_livre)                                             #Converte a string da posição para posição

                if eh_posicao(a) and eh_posicao_valida(a, obtem_numero_orbitas(t)):         #Verifica se a posição convertida é válida e se está dentro do número de órbitas
                    if obtem_pedra(t, a) == cria_pedra_neutra():                            #Verifica se a posição escolhida está livre
                        return a          
    
def escolhe_movimento_auto(t, j, lvl):
    if lvl == "facil":
        tab_original = cria_copia_tabuleiro(t)
        tab_rodado = roda_tabuleiro(tab_original)
        n = obtem_numero_orbitas(t)
        posicoes_jogaveis = ()
        posicoes_livres = ()
        r = ()
        for i in obtem_posicoes_pedra(tab_rodado, j):                                               #Itera sobre as posições onde o jogador j tem pedras
            for x in obtem_posicoes_adjacentes(i, n, True):                                         #Para cada posição, obtém as posições adjacentes
                if obtem_pedra(tab_rodado, cria_posicao(x[0], x[1])) == cria_pedra_neutra():        #Verifica se a posição adjacente está livre
                    posicoes_jogaveis = posicoes_jogaveis + (x, )                                   #Adiciona a posição adjacente jogável
        
        for i in range(len(posicoes_jogaveis)):                                                     #Cria um tuplo r com as posições seguintes para cada posição jogável
            r = r + (obtem_posicao_seguinte(tab_rodado, posicoes_jogaveis[i], True), )
        if r != ():                                                                                 #Se esse tuplo não estiver vazio
                return ordena_posicoes(r, n)[0]         
        else:
            for i in tab_pos_tuplo(n):                                                              #Se não há movimentos jogáveis, procura posições livres no tabuleiro original
                if obtem_pedra(tab_original, i) == cria_pedra_neutra():
                    posicoes_livres = posicoes_livres + (cria_posicao(i[0], i[1]) ,)
            return ordena_posicoes(posicoes_livres, n)[0]         
    


    
    elif lvl == "normal":

        tab_original = cria_copia_tabuleiro(t)
        tab_contra = cria_copia_tabuleiro(t)
        n = obtem_numero_orbitas(t)
        k = obtem_dimensoes(n)
        maior_L = 0
        pos_maior_L = ()
        maior_L_contra = 0
        pos_maior_L_contra = ()
        r = ()
        posicoes_livres_1x = ()
        posicoes_livres_2x = ()

        roda_tabuleiro(tab_original)

        #Posiçoes livre do tab original
        for i in tab_pos_tuplo(n):
                if obtem_pedra(tab_original, i) == cria_pedra_neutra():
                    posicoes_livres_1x = posicoes_livres_1x + (cria_posicao(i[0], i[1]) ,)

        #Define a pedra do oponente com base na pedra do jogador
        if j == cria_pedra_branca():
            contra = cria_pedra_preta()                             #Oponente é a pedra preta
        else:
            contra = cria_pedra_branca()                            #Oponente é a pedra branca
                    
        for i in posicoes_livres_1x:
            tabela_prov = coloca_pedra(tab_original, i, j)          #Coloca a pedra do jogador na posição livre
            
            for x in range(k , 0, -1):                              #Verifica linhas de tamanho x, de k a 1
                if verifica_linha_pedras(tabela_prov, i, j, x):      
                    if maior_L < x:                                  #Se uma nova maior linha é encontrada
                        maior_L = x
                        pos_maior_L = (i, )                         #Atualiza a posição da maior linha
                    elif maior_L == x:                              #Se uma linha igual à maior encontrada
                        pos_maior_L = pos_maior_L + (i, )           #Adiciona à lista de posições
            remove_pedra(tabela_prov,i)                             #Remove a pedra do jogador da simulação

        roda_tabuleiro(tab_contra)
        roda_tabuleiro(tab_contra)

        #Encontra posições livres no tabuleiro do oponente
        for i in tab_pos_tuplo(n):
                if obtem_pedra(tab_contra, i) == cria_pedra_neutra():
                    posicoes_livres_2x = posicoes_livres_2x + (cria_posicao(i[0], i[1]) ,)
        
        for i in posicoes_livres_2x:
            tabela_prov = coloca_pedra(tab_contra, i, contra)               #Coloca a pedra do oponente na posição livre
            for x in range(k , 0, -1):
                if verifica_linha_pedras(tabela_prov, i, contra, x):        #Verifica linhas de tamanho x, de k a 1
                    if maior_L_contra < x:                                  #Se uma nova maior linha é encontrada
                        maior_L_contra = x
                        pos_maior_L_contra = (i,)                           #Atualiza a posição da maior linha
                    elif maior_L_contra == x:                               #Se uma linha igual à maior encontrada
                        pos_maior_L_contra = pos_maior_L_contra + (i, )     #Adiciona à lista de posições
            remove_pedra(tabela_prov,i)                                     #Remove a pedra do oponente da simulação
        
        if maior_L >= maior_L_contra:
            for i in pos_maior_L:
                a = obtem_posicao_seguinte(tab_original, i, True)       #Obtém a próxima posição para o jogador
                r = r + (a, )                                           #Adiciona à lista de resultados
            return ordena_posicoes(r, n)[0]
        else:
            for i in pos_maior_L_contra:
                a = obtem_posicao_seguinte(tab_original, i, True)       #Obtém a próxima posição para o oponente
                b = obtem_posicao_seguinte(tab_original, a, True)       #Obtém a próxima posição depois
                r = r + (b, )                                           #Adiciona à lista de resultados
            return ordena_posicoes(r, n)[0]

def orbito(n, modo, jog):
    
    if type(n) != int or type(modo) != str or type(jog) != str:
        raise ValueError("orbito: argumentos invalidos")
    if n > 5 or n < 2:
        raise ValueError("orbito: argumentos invalidos")
    if modo not in ("facil", "normal", "2jogadores"):
        raise ValueError("orbito: argumentos invalidos")
    if jog not in (cria_pedra_preta(), cria_pedra_branca()):
        raise ValueError("orbito: argumentos invalidos")
    m = str(n)
    print("Bem-vindo ao ORBITO-" + m +".")
    
    t = cria_tabuleiro_vazio(n)
    if modo in ("facil", "normal"):    
        print("Jogo contra o computador (" + modo + ").")
        if jog == cria_pedra_preta():
            jog_contra = cria_pedra_branca()
            print("O jogador joga com 'X'.")
            print(tabuleiro_para_str(cria_tabuleiro_vazio(n)))
            while True:
                print("Turno do jogador.")
                a = escolhe_movimento_manual(t)
                coloca_pedra(t, str_para_posicao(a), jog)
                
                if eh_vencedor(t, jog) and not eh_vencedor(t, jog_contra):
                    print(tabuleiro_para_str(t))
                    print("VITORIA")
                    if jog == cria_pedra_preta():
                        return pedra_para_int(cria_pedra_preta())
                    else:
                        return pedra_para_int(cria_pedra_branca())
                if eh_vencedor(t, jog_contra) and not eh_vencedor(t, jog):
                    print(tabuleiro_para_str(t))
                    print("DERROTA")
                    if jog == cria_pedra_preta():
                        return pedra_para_int(cria_pedra_preta())
                    else:
                        return pedra_para_int(cria_pedra_branca())    
                if eh_fim_jogo(t):
                    print(tabuleiro_para_str(t))
                    print("EMPATE")
                    return pedra_para_int(cria_pedra_neutra())
                roda_tabuleiro(t)
                print(tabuleiro_para_str(t))
                if eh_vencedor(t, jog) and not eh_vencedor(t, jog_contra):
                    print("VITORIA")
                    if jog == cria_pedra_preta():
                        return pedra_para_int(cria_pedra_preta())
                    else:
                        return pedra_para_int(cria_pedra_branca())
                if eh_vencedor(t, jog_contra) and not eh_vencedor(t, jog):
                    print("DERROTA")
                    if jog == cria_pedra_preta():
                        return pedra_para_int(cria_pedra_preta())
                    else:
                        return pedra_para_int(cria_pedra_branca()) 
                if eh_fim_jogo(t):
                    print("EMPATE")
                    return pedra_para_int(cria_pedra_neutra())
                print("Turno do computador (" + modo + "):")
                a = escolhe_movimento_auto(t, jog_contra, modo)
                coloca_pedra(t,str_para_posicao(a) ,jog_contra)
                
                if eh_vencedor(t, jog_contra) and not eh_vencedor(t, jog):
                    print(tabuleiro_para_str(t))
                    print("DERROTA")
                    if jog_contra == cria_pedra_preta():
                        return pedra_para_int(cria_pedra_preta())
                    else:
                        return pedra_para_int(cria_pedra_branca())
                if eh_vencedor(t, jog) and not eh_vencedor(t, jog_contra):
                    print(tabuleiro_para_str(t))
                    print("VITORIA")
                    if jog_contra == cria_pedra_preta():
                        return pedra_para_int(cria_pedra_preta())
                    else:
                        return pedra_para_int(cria_pedra_branca()) 
                if eh_fim_jogo(t):
                    print(tabuleiro_para_str(t))
                    print("EMPATE")
                    return pedra_para_int(cria_pedra_neutra())
                roda_tabuleiro(t)
                print(tabuleiro_para_str(t))
                if eh_vencedor(t, jog_contra) and not eh_vencedor(t, jog):
                    print(tabuleiro_para_str(t))
                    print("DERROTA")
                    if jog_contra == cria_pedra_preta():
                        return pedra_para_int(cria_pedra_preta())
                    else:
                        return pedra_para_int(cria_pedra_branca())
                if eh_fim_jogo(t):
                    print(tabuleiro_para_str(t))
                    print("EMPATE")
                    return pedra_para_int(cria_pedra_neutra())
                
    
        elif jog == cria_pedra_branca():
            jog_contra = cria_pedra_preta()
            print("O jogador joga com 'O'.")
            print(tabuleiro_para_str(cria_tabuleiro_vazio(n)))
            while True:
                print("Turno do computador (" + modo + "):")
                a = escolhe_movimento_auto(t, jog_contra ,modo)
                coloca_pedra(t, str_para_posicao(a), jog_contra)
                
                # if eh_vencedor(t, jog_contra) and not eh_vencedor(t, jog):
                #     print(tabuleiro_para_str(t))
                #     print("DERROTA")
                #     if jog_contra == cria_pedra_preta():
                #         return pedra_para_int(cria_pedra_preta())
                #     else:
                #         return pedra_para_int(cria_pedra_branca()) 
                # if eh_vencedor(t, jog) and not eh_vencedor(t, jog_contra):
                #     print(tabuleiro_para_str(t))
                #     print("VITORIA")
                #     if jog == cria_pedra_preta():
                #         return pedra_para_int(cria_pedra_preta())
                #     else:
                #         return pedra_para_int(cria_pedra_branca())    
                # if eh_fim_jogo(t):
                #     print(tabuleiro_para_str(t))
                #     print("EMPATE")
                #     return pedra_para_int(cria_pedra_neutra())
                roda_tabuleiro(t)
                print(tabuleiro_para_str(t))
                if eh_vencedor(t, jog_contra) and not eh_vencedor(t, jog):
                    print("DERROTA")
                    if jog_contra == cria_pedra_preta():
                        return pedra_para_int(cria_pedra_preta())
                    else:
                        return pedra_para_int(cria_pedra_branca())
                if eh_vencedor(t, jog) and not eh_vencedor(t, jog_contra):
                    print("VITORIA")
                    if jog == cria_pedra_preta():
                        return pedra_para_int(cria_pedra_preta())
                    else:
                        return pedra_para_int(cria_pedra_branca())   
                if eh_fim_jogo(t):
                    print("EMPATE")
                    return pedra_para_int(cria_pedra_neutra())
                
                print("Turno do jogador.")
                coloca_pedra(t, escolhe_movimento_manual(t), jog)
                # if eh_vencedor(t, jog) and not eh_vencedor(t, jog_contra):
                #     print(tabuleiro_para_str(t))
                #     print("VITORIA")
                #     if jog == cria_pedra_preta():
                #         return pedra_para_int(cria_pedra_preta())
                #     else:
                #         return pedra_para_int(cria_pedra_branca()) 
                # if eh_vencedor(t, jog_contra) and not eh_vencedor(t, jog):
                #     print(tabuleiro_para_str(t))
                #     print("DERROTA")
                #     if jog_contra == cria_pedra_preta():
                #         return pedra_para_int(cria_pedra_preta())
                #     else:
                #         return pedra_para_int(cria_pedra_branca()) 
                # if eh_fim_jogo(t):
                #     print(tabuleiro_para_str(t))
                #     print("EMPATE")
                #     return pedra_para_int(cria_pedra_neutra())
                roda_tabuleiro(t)
                print(tabuleiro_para_str(t))
                if eh_vencedor(t, jog) and not eh_vencedor(t, jog_contra):
                    print("VITORIA")
                    if jog == cria_pedra_preta():
                        return pedra_para_int(cria_pedra_preta())
                    else:
                        return pedra_para_int(cria_pedra_branca())
                if eh_vencedor(t, jog_contra) and not eh_vencedor(t, jog):
                    print(tabuleiro_para_str(t))
                    print("DERROTA")
                    if jog_contra == cria_pedra_preta():
                        return pedra_para_int(cria_pedra_preta())
                    else:
                        return pedra_para_int(cria_pedra_branca())
                if eh_fim_jogo(t):
                    print("EMPATE")
                    return pedra_para_int(cria_pedra_neutra())
                
                
    elif modo == "2jogadores":
        print("Jogo para dois jogadores.")
        print(tabuleiro_para_str(t))
        while True:
            
            print("Turno do jogador 'X'.")
            
            a = escolhe_movimento_manual(t)
            coloca_pedra(t, str_para_posicao(a), cria_pedra_preta())
            
            # if eh_vencedor(t, cria_pedra_preta()) and not eh_vencedor(t, cria_pedra_branca()):
            #     print(tabuleiro_para_str(t))
            #     print("VITORIA DO JOGADOR 'X'")
            #     return pedra_para_int(cria_pedra_preta())
            # if eh_vencedor(t, cria_pedra_branca()) and not eh_vencedor(t, cria_pedra_preta()):
            #     print(tabuleiro_para_str(t))
            #     print("VITORIA DO JOGADOR 'O'")
            #     return pedra_para_int(cria_pedra_branca())
            # if eh_fim_jogo(t):
            #     print(tabuleiro_para_str(t))
            #     print("EMPATE")
            #     return pedra_para_int(cria_pedra_neutra())
            
            roda_tabuleiro(t)
            print(tabuleiro_para_str(t))

            if eh_vencedor(t, cria_pedra_preta()) and not eh_vencedor(t, cria_pedra_branca()):
                print("VITORIA DO JOGADOR 'X'")
                return pedra_para_int(cria_pedra_preta())
            if eh_vencedor(t, cria_pedra_branca()) and not eh_vencedor(t, cria_pedra_preta()):                
                print("VITORIA DO JOGADOR 'O'")
                return pedra_para_int(cria_pedra_branca())
            if eh_fim_jogo(t):                
                print("EMPATE")
                return pedra_para_int(cria_pedra_neutra())
            
            print("Turno do jogador 'O'.")
            a = escolhe_movimento_manual(t)
            coloca_pedra(t, str_para_posicao(a), cria_pedra_branca())
            
            # if eh_vencedor(t, cria_pedra_branca()) and not eh_vencedor(t, cria_pedra_preta()):
            #     print(tabuleiro_para_str(t))
            #     print("VITORIA DO JOGADOR 'O'")
            #     return pedra_para_int(cria_pedra_branca())
            # if eh_vencedor(t, cria_pedra_preta()) and not eh_vencedor(t, cria_pedra_branca()):
            #     print(tabuleiro_para_str(t))
            #     print("VITORIA DO JOGADOR 'X'")
            #     return pedra_para_int(cria_pedra_preta())
            # if eh_fim_jogo(t):
            #     print(tabuleiro_para_str(t))
            #     print("EMPATE")
            #     return pedra_para_int(cria_pedra_neutra())
            
            roda_tabuleiro(t)
            print(tabuleiro_para_str(t))

            if eh_vencedor(t, cria_pedra_branca()) and not eh_vencedor(t, cria_pedra_preta()):
                print("VITORIA DO JOGADOR 'O'")
                return pedra_para_int(cria_pedra_branca())
            if eh_vencedor(t, cria_pedra_preta()) and not eh_vencedor(t, cria_pedra_branca()):
                print("VITORIA DO JOGADOR 'X'")
                return pedra_para_int(cria_pedra_preta())
            if eh_fim_jogo(t):
                print("EMPATE")
                return pedra_para_int(cria_pedra_neutra())

            
            

        

        





