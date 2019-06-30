# Смежность вершин
inc = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [],
    4: [7, 8],
    5: [9, 10],
    6: [],
    7: [11, 12],
    8: [],
    9: [],
    10: [],
    11: [],
    12: []
}

visited = set() # Посещена ли вершина ?
Q = []  # Очередь
BFS = []

# Поиск в ширину - bfs
def bfs(v):
    if v in visited: # Если вершина уже посещена, выходим
        return
    visited.add(v) # Посетили вершину v
    BFS.append(v) # запоминаем порядок обхода
    for i in inc[v]: # Все сможные с v вершины
        if not i in visited:
            Q.append(i)
    while Q:
        bfs(Q.pop(0))

start = 1
bfs(start) # начальная вершина обхода
print(BFS)