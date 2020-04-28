def lit_grille(string):
    arr = [[0 for i in range(9)] for j in range(9)]
    x, y = 0, 0
    
    for c in s:
        if y == 9:
            break
        if x == 9:
            x = 0
            y += 1
        if c == '.':
            arr[y][x] = None
        else:
            arr[y][x] = int(c)
        x += 1
    return (arr)

def affiche_grille(array):
    for i in range(9):
        for j in range(9):
            if arr[i][j] == None:
                print('.', end=' ')
            else:
                print(arr[i][j], end=' ')
        print('\n')
        
def possibles (G ,i , j ):
    # valeurs pr´e sentes sur la ligne i
    L = set(G[i][k] for k in range (9))
    # valeurs pr´e sentes sur la colonne j
    C = set(G[k][j] for k in range (9))
    # valeurs pr´e sentes dans la sous - grille contenant la case (i,j)
    i0 , j0 = i - (i % 3), j - (j % 3)
    S = set( G [ i0 + k ][ j0 + l ] for k in range (3) for l in range (3))
    return {1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9} - L.union(C).union(S)
        
s = "2.69.4.....5..69878....5..23..6..25.65.....73.91..3..45..1....81634..7.....5.74.6"
arr = lit_grille(s)
#affiche_grille(arr)
possibles(arr, 1, 0)
