def lit_grille(s):
    G = [[0 for i in range(9)] for j in range(9)]
    x, y = 0, 0
    
    for c in s:
        if y == 9:
            break
        if x == 9:
            x = 0
            y += 1
        if c == '.':
            G[y][x] = None
        else:
            G[y][x] = int(c)
        x += 1
    return (G)

def affiche_grille(G):
    for i in range(9):
        for j in range(9):
            if G[i][j] == None:
                print('.', end=' ')
            else:
                print(G[i][j], end=' ')
        print()
        
def possibles(G ,i , j ):
    # valeurs pr´e sentes sur la ligne i
    L = set(G[i][k] for k in range (9))
    # valeurs pr´e sentes sur la colonne j
    C = set(G[k][j] for k in range (9))
    # valeurs pr´e sentes dans la sous - grille contenant la case (i,j)
    i0 , j0 = i - (i % 3), j - (j % 3)
    S = set( G [ i0 + k ][ j0 + l ] for k in range (3) for l in range (3))
    return {1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9} - L.union(C).union(S)

def résoudre(G):
    for i in range(9):
        for j in range(9):
            if G[i][j] == None:
                for x in possibles(G, i, j):
                    print("i = ", i, " j = ", j, " x = ", x, possibles(G, i, j))
                    G[i][j] = x
                    if résoudre(G):
                        return (True)
                G[i][j] == None
                return (False)
    return (True)

s = "2.69.4.....5..69878....5..23..6..25.65.....73.91..3..45..1....81634..7.....5.74.6"
G = lit_grille(s)
affiche_grille(G)
print()
print(possibles(G, 1, 3))
print(résoudre(G))
print()
affiche_grille(G)
