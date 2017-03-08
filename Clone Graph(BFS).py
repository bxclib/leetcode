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
        self.mapbfs={}
        self.ll=[node]
        n=0
        while n!=-1:
            if n==0:
                n=self.bfs(node)
                m=n
            else:
                n=self.bfs(node)
        for i,j in self.mapbfs.items():
            self.mapbfs[i][0].neighbors=[]
            for s in self.mapbfs[i][1]:
                self.mapbfs[i][0].neighbors.append(self.mapbfs[s.label][0])
                
            
        return m
    def bfs(self,node):
        if self.ll!=[]:
            node=self.ll[0]
            del self.ll[0]
        else:
            return -1
        node2=UndirectedGraphNode(node.label)
        self.mapbfs[node.label]=(node2,node.neighbors)
        node.isvisit=True
        for i in node.neighbors:
            if hasattr(i, "isvisit") is False:
                
                self.ll.append(i)
        return node2

