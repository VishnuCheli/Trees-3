#Time Complexity:: O(n)-all nodes are visited in once
#Space Complexity:: O(1)-no extra space used
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
# Definition for singly-linked list

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max = root.val #the maximum value at the start is the root node
        self.recur(root) #recur function
        return self.max #returning the global max path sum
    
    def recur(self,root): 
        #base
        if root == None: #if null node is visited return a sum of 0
            return 0
        
        #logic
        leftsum = max(self.recur(root.left),0) #every left branches root val is retrieved
        rightsum = max(self.recur(root.right),0) #every right branches root val is retrieved
        
        rootmax = root.val + leftsum + rightsum #the current nodes maximum is calculated with child node values
        
        if self.max < rootmax: #whenever a new pat with larger max path sum
            self.max = rootmax #change the max path global variable to current path traverse max
        
        return root.val + max(leftsum, rightsum) #return the current nodes val + the max of left/right branch