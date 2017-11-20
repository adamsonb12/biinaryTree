# ## Node

# Each node of the binary tree should be an instance of your `Node` class.  Create this class with the following fields:

# 1. `key` - the key the item is stored under.  The placement of the node in the tree is based on this key.
# 1. `value` - the value being stored (string or object is fine).
# 1. `parent` - a reference to the parent of the node.
# 1. `left` - a reference to the left child of the node.
# 1. `right` - a reference to the right child of the node.

class Node(object):
    '''A node in a binary tree'''

    def __init__(self, key, value, parent=None, left=None, right=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        
    def __str__(self):
        return '<Node: {}:{}>'.format(self.key, self.value)

    

