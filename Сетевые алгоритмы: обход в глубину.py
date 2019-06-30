tree = [[1, 2, 3],
        [4, 5],
        [],
        [6, 7],
        [8, 9],
        [],
        [10, 11],
        [],
        [],
        [],
        [],
        []]

DFS = [0]


def dfs(v):
    if len(tree[v]) == 0:
        return
    else:
        for i in tree[v]:
            DFS.append(i)
            dfs(i)


dfs(0)
print(DFS)
