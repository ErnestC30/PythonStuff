#Creating a binary search tree and using it.
import random

class Node(object):
    """Node object to keep track of parent and child nodes"""
    def __init__(self, val):
        self.val    = val
        self.left   = None
        self.right  = None
        self.parent = None

class BinarySearchTree(object):
    """Binary Search Tree object to hold nodes, and contains tree methods"""
    def __init__(self):
        self.root = None

    def insert(self, val):
        """Inserts the given value into the tree following BST rules"""
        if self.root == None:
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, cur_node):
        if cur_node.val == val:
            return
        #New value is higer than current node
        if cur_node.val < val:                  
            if cur_node.right == None:
                cur_node.right = Node(val)
                cur_node.right.parent = cur_node
            else:
                self._insert(val, cur_node.right)
        #New value is lower than current node
        if cur_node.val > val:                  
            if cur_node.left == None:
                cur_node.left = Node(val)
                cur_node.left.parent = cur_node
            else:
                self._insert(val, cur_node.left)

    def getMaxDepth(self):
        """Prints out the maximum depth of the tree"""
        if self.root == None:
            return 0
        else:
            depth = self._getDepth(self.root, 0)
            print(f'The depth of the tree is {depth}')

    def _getDepth(self, cur_node, depth):
        depth += 1
        #No more child nodes
        if cur_node.left == None and cur_node.right == None:        
            return depth
        #Only right child
        if cur_node.left == None:                                  
            return self._getDepth(cur_node.right, depth)
        #Only left child
        if cur_node.right == None:                                  
            return self._getDepth(cur_node.left, depth)
        #Two child nodes. Return the higher depth value between the two branches
        else:
            depth = max(self._getDepth(cur_node.right, depth), self._getDepth(cur_node.left, depth))
            return depth

    def display(self):
        """Print the binary search tree as a tree structure"""
        lines, *_ = self._display_aux(self.root)
        for line in lines:
            print(line)

    def _display_aux(self, cur_node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if cur_node.right is None and cur_node.left is None:
            line = '%s' % cur_node.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if cur_node.right == None:
            lines, n, p, x = self._display_aux(cur_node.left)
            s = '%s' % cur_node.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if cur_node.left == None:
            lines, n, p, x = self._display_aux(cur_node.right)
            s = '%s' % cur_node.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(cur_node.left)
        right, m, q, y = self._display_aux(cur_node.right)
        s = '%s' % cur_node.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def convertToList(self):
        """Convert the binary search tree into a sorted list structure"""
        treelist = self._convertToList(self.root)
        print(f'The tree converted to list is: {treelist}')
        return treelist

    def _convertToList(self, node):
        if node is None:
            return []
        return self._convertToList(node.left) + [node.val] + self._convertToList(node.right)

    def rangeSum(self, low, high):
        """Returns the sum of all values in the tree that are between the low and high value."""
        treelist = self._convertToList(self.root)
        return sum(num for num in treelist if num > low and num < high)



    
        
def createTree(size,max_val):
    """Returns a binary search tree object"""
    tree = BinarySearchTree()             
    #Keep track of values to ensure no dupes          
    values = []                                     
    for _ in range(size):
        dupe = True
        #Generate unique values for each node
        while dupe:                                 
            val = random.randint(1,max_val)     
            if val not in values:
                values.append(val)
                tree.insert(val)
                dupe = False
    return tree


tree = createTree(10, 50)
tree.display()
tree.convertToList()
print(tree.rangeSum(10,30))
#tree.getMaxDepth()