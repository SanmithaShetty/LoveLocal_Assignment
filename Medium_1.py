
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lca(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        #if the root itself is one of the two p and q then return root
        if (root == p or root == q or not root): 
            return root 
        
        #call recursion on itself 
        l = self.lca(root.left, p, q)
        r = self.lca(root.right, p, q) 
        
        if l and r: #common ancestor has been found, return the root of the two
            return root    
        elif l: 
            return l
        elif r: 
            return r
        
def main():
    # Creating the tree
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    # Nodes to find LCA for
    p = root.left  # Node with value 2
    q = root.left.right  # Node with value 8

    # Creating an instance of the Solution class
    solution = Solution()

    # Calling the lca function
    result = solution.lca(root, p, q)

    # Displaying the result
    print("The Lowest Common Ancestor of nodes {} and {} is: {}".format(p.val, q.val, result.val if result else None))

if __name__ == "__main__":
    main()
