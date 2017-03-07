# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        #print node.neighbors
        self.mapdfs={}
        n=self.dfs(node)
        for i,j in self.mapdfs.items():
            self.mapdfs[i][0].neighbors=[]
            for s in self.mapdfs[i][1]:
                self.mapdfs[i][0].neighbors.append(self.mapdfs[s.label][0])
                
            
        return n
    def dfs(self,node):
        node2=UndirectedGraphNode(node.label)
        self.mapdfs[node.label]=(node2,node.neighbors)
        node.isvisit=True
        for i in node.neighbors:
            if hasattr(i, "isvisit") is False:
                
                self.dfs(i)
        return node2
