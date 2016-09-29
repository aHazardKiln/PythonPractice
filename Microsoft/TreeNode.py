class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self,val):
        self.root = TreeNode(val)

    def insert(self,val):
        self._insert(self.root,val)

    def _insert(self,node,val):
        if val <= node.val:
            if node.left is not None:
                self._insert(node.left,val)
            else:
                node.left = TreeNode(val)
        else:
            if node.right is not None:
                self._insert(node.right,val)
            else:
                node.right = TreeNode(val)
    def print_inorder(self):
        self._print_inorder(self.root)
    def _print_inorder(self,node):
        if node is None:
            return
        self._print_inorder(node.left)
        print str(node.val),
        self._print_inorder(node.right)
    def print_inorder_iterative(self):
        self._print_inorder_iterative(self.root)
    def _print_inorder_iterative(self,node):
        l = []
        while node is not None:
            l.append(node)
            node = node.left
        while (len(l)!=0):
            node = l.pop(-1)
            print node.val,
            node = node.right
            while node is not None:
                l.append(node)
                node = node.left

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self,node):
        if node is None:
            return
        print node.val,
        self._preorder(node.left)
        self._preorder(node.right)

    def preorder_iterative(self):
        self._preorder_iterative(self.root)

    def  _preorder_iterative(self,node):
        #push the left line to stack and print
        l = []
        while node is not None:
            while node is not None:
                l.append(node)
                print node.val,
                node = node.left

        while (len(l)!=0):
            node = l.pop(-1)
            node = node.right
            while node is not None:
                l.append(node)
                print node.val,
                node = node.left



if __name__ == "__main__":
    root = Tree(6)
    root.insert(4)
    root.insert(10)
    root.insert(-1)
    root.insert(5)
    root.preorder_iterative()


    '''
        6
      /  \
      4   10
    -1  5
        '''