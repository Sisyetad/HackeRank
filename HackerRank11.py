class CutTheTree:
    #https://www.hackerrank.com/challenges/cut-the-tree/problem?isFullScreen=true
    def cutTheTree(data, edges):
        # Write your code here
        tree = [[] for i in range(len(data))]
        for edge in edges:
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])
        return tree