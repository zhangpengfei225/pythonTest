class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self,root,x,height,parent):
        if root == None:
            return 0,None
        if root.val  == x:
            return height,parent
        heightresult,parent = self.dfs(root.left,x,height+1,root)
        if heightresult==0:
            heightresult,parent = self.dfs(root.right,x,height+1,root)
        
        return heightresult,parent
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        #print(self.dfs(root,x,1,None))
        #print(self.dfs(root,y,1,None))
        return self.dfs(root,x,1,None)[0]==self.dfs(root,y,1,None)[0] and self.dfs(root,x,1,None)[1]!=self.dfs(root,y,1,None)[1]

root = TreeNode(1)  
root.left = TreeNode(2)   
left1  = root.left
left1.left = TreeNode(4)  
root.right = TreeNode(3)  
right1 = root.right
right1.left= TreeNode(5)
s = Solution()
print(s.isCousins(root,4,3))