#Creating a binary search tree and using it.
import random

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        """Inserts the given value into the tree following BST rules"""
        if self.val == val:
            return
        if self.val < val:                  #New value is higer than current node
            if self.right == None:
                self.right = Node(val)
            else:
                self.right.insert(val)
        if self.val > val:                  #New value is lower than current node
            if self.left == None:
                self.left = Node(val)
            else:
                self.left.insert(val)

    def getDepth(self):
        pass

    def display(self):
        """Print the binary search tree as a tree structure"""
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right == None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left == None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
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


def createTree(size,max_val):
    root = Node(random.randint(1,max_val))          #Initialize the root node
    values = [root.val]
    for i in range(size-1):
        dupe = True
        while dupe:                                 #Generate unique vales for each node
            val = random.randint(0,max_val)     
            if val not in values:
                values.append(val)
                root.insert(val)
                dupe = False
    return root

tree = createTree(10,50)
tree.display()