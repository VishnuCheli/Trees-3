#Time Complexity:: O(n)-all nodes visited
#Space Complexity:: O(H)-RS space
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.flag = True
        self.recur(root) #passing the root node into the recur method
        return self.flag #returning the final
        
        
    def recur(self,root):
        #base condition
        if root==None: #there is no node so root is null
            return 0
        
        #action
        leftht = self.recur(root.left) #finding the left of node height
        rightht = self.recur(root.right) #finding the right of node height
        
        if abs(leftht-rightht)>1: #checking condition to see if the tree is unbalanced
            self.flag = False 
        
        return 1+max(leftht,rightht) #1 + the max among left and right sub tree as the height of the tree depends on both left and right branches