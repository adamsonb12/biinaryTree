import unittest
from node import Node
# # Assignment: Binary Tree

# Write a binary tree class that has the following methods:

class BinaryTree(object):
    ''' A Binary Tree Data Structure '''

    def __init__(self):
        self.root = Node('', '')

    # 1. `set(key, value)` stores a key=value pair to the tree in the appropriate spot.
    def __set__(self, key, value):
        node = self.root
        if(node.value == '' and node.key == ''):
            node.key = key
            node.value = value
        else:
            while(node.value != value):
                if(node.key == key):
                    node.value = value
                elif(key < node.key):
                    if(node.left is None):
                        node.left = Node(key, value, node)
                    node = node.left
                elif(key > node.key):
                    if(node.right is None):
                        node.right = Node(key, value, node)
                    node = node.right

    # 2. `get(key)` returns the value stored with the given key.  If the key does not exist, null/None should be returned.
    def get(self, key):
        node = self.__findNode__(key)
        return node.value

    def __findNode__(self, key):
        node = self.root
        while (node.key != key):
            if(key < node.key):
                if(node.left is None):
                    return (str(key) + ' does not exist in the tree')
                else:
                    node = node.left
            elif(key > node.key):
                if(node.right is None):
                    return (str(key) + ' does not exist in the tree')
                else:
                    node = node.right
        return node

    # 3. `remove(key)` removes the node with the given key from the tree.  If the key does not exist, it should simply return (no error).
    def remove(self, key):
        node = self.__findNode__(key)
        if(node.left is None and node.right is None):
            self.__remove_leaf__(key)
        elif( (node.left is None and node.right is not None) or (node.left is not None and node.right is None)):
            self.__remove_node_one_child(key)
        else:
            node2 = node.left
            while(node2.right is not None):
                node2 = node2.right
            # delete node replacing deleted node
            temp = node2
            self.remove(node2.key)
            # replace deleted node with new node
            node.key = temp.key
            node.value = temp.value
            
    def __remove_leaf__(self, key):
        node = self.__findNode__(key)
        parent = node.parent
        if(parent.left is node):
            parent.left = None
        else:
            parent.right = None

    def __remove_node_one_child(self, key):
        node = self.__findNode__(key)
        parent = node.parent
        if(parent.left is node):
            if(node.left is None):
                parent.left = node.right
                node.right.parent = parent
            else:
                parent.left = node.left
                node.left.parent = parent
        else:
            if(node.right is None):
                parent.right = node.left
                node.left.parent = parent
            else:
                parent.right = node.right
                node.right.parent = parent

    # 8. `debug_print()` prints a graphical representation of the tree. See below for more information.
    def debug_print(self):
        q = []
        if(self.root is None):
            return
        q.append(self.root)
        while(len(q) > 0):
            node = q[0]
            if(node.left is not None):
                q.append(node.left)
            if(node.right is not None):
                q.append(node.right)

            if(node.parent is None):
                print(str(node.key) + '(-)')    
            else:
                print(str(node.key) + '(' + str(node.parent.key) + ')')
            q.pop(0)
        return

    # 5. `walk_dfs_preorder()` iterates through the nodes of the tree in depth-first-search "preorder" order.
    def walk_dfs_preorder(self, node):
        if(node is not None):
            print(str(node.value))
            self.walk_dfs_preorder(node.left)
            self.walk_dfs_preorder(node.right)

     # 4. `walk_dfs_inorder()` iterates through the nodes of the tree in depth-first-search "inorder" order.
    def walk_dfs_inorder(self, node):
        if(node is not None):
            self.walk_dfs_inorder(node.left)
            print(node.value)
            self.walk_dfs_inorder(node.right)

    # 6. `walk_dfs_postorder()` iterates through the nodes of the tree in depth-first-search "postorder" order.
    def walk_dfs_postorder(self, node):
        if(node is not None):
            self.walk_dfs_postorder(node.left)
            self.walk_dfs_postorder(node.right)
            print(node.value)

    # 7. `walk_bfs()` iterates through the nodes of the tree in breadth-first-search order.
    def walk_bfs(self):
        q = []
        l = []
        if(self.root is None):
            return
        q.append(self.root)
        l.append(self.root)
        while(len(q) > 0):
            node = q[0]
            if(node.left is not None):
                q.append(node.left)
                l.append(node.left)
            if(node.right is not None):
                q.append(node.right)
                l.append(node.right)
            q.pop(0)
        return l



#######################################################
### A Testing Class for the Binary Treet

class TestLinkedList(unittest.TestCase):
    """ Testing methods that test each function in the circular linked list class """
    def set_up(self):
        self.bt = BinaryTree()

    def test_set_numbers(self):
        self.set_up()
        bt = self.bt
        bt.__set__(10, 10)
        self.assertEquals(bt.__findNode__(10).key, 10)
        bt.__set__(9, 9)
        self.assertEquals(bt.__findNode__(9).key, 9)
        bt.__set__(13, 13)
        self.assertEquals(bt.__findNode__(13).key, 13)
        bt.__set__(12, 12)
        self.assertEquals(bt.__findNode__(12).key, 12)
        bt.__set__(6, 6)
        self.assertEquals(bt.__findNode__(6).key, 6)
        bt.__set__(7, 7)
        self.assertEquals(bt.__findNode__(7).key, 7)

    def test_get(self):
        self.set_up()
        bt = self.bt
        bt.__set__(10, 10)
        self.assertEquals(bt.get(10), 10)
        bt.__set__(9, 9)
        self.assertEquals(bt.get(9), 9)
        bt.__set__(13, 13)
        self.assertEquals(bt.get(13), 13)
        bt.__set__(12, 12)
        self.assertEquals(bt.get(12), 12)
        bt.__set__(6, 6)
        self.assertEquals(bt.get(6), 6)
        bt.__set__(7, 7)
        self.assertEquals(bt.get(7), 7)

    def test_remove_leaf(self):
        self.set_up()
        bt = self.bt
        bt.__set__(10, 10)
        bt.__set__(9, 9)
        bt.__set__(13, 13)
        bt.__set__(12, 12)
        bt.__set__(6, 6)
        bt.__set__(7, 7)
        # Delete leaf
        self.assertEquals(bt.__findNode__(7).key, 7) # Makes sure it's there first
        bt.remove(7)
        self.assertEquals(bt.__findNode__(6).right, None)

    def test_remove_node_with_one_child(self):
        self.set_up()
        bt = self.bt
        bt.__set__(10, 10)
        bt.__set__(9, 9)
        bt.__set__(11, 11)
        bt.__set__(6, 6)
        bt.__set__(4, 4)
        bt.__set__(12,12)
        bt.__set__(7,7)
        bt.remove(9)
        self.assertEquals(bt.__findNode__(10).left.key, 6)
        self.assertEquals(bt.__findNode__(6).left.key, 4)
        self.assertEquals(bt.__findNode__(6).right.key, 7)
        self.assertEquals(bt.root.left.key, 6)
        bt.remove(11)
        self.assertEquals(bt.__findNode__(10).right.key, 12)
        self.assertEquals(bt.__findNode__(12).left, None)
        self.assertEquals(bt.root.right.key, 12)

    def test_remove_node_with_multiple_children(self):
        self.set_up()
        bt = self.bt
        bt.__set__(10, 10)
        bt.__set__(9, 9)
        bt.__set__(6, 6)
        bt.__set__(4, 4)
        bt.__set__(7,7)
        bt.__set__(1,1)
        bt.__set__(5,5)
        bt.__set__(6.5,6.5)
        bt.__set__(8,8)
        bt.__set__(16,16)
        bt.__set__(17,17)
        bt.__set__(11,11)
        bt.__set__(15,15)
        bt.__set__(14,14)
        bt.__set__(12,12)
        bt.remove(6)
        self.assertEquals(bt.__findNode__(5).left.key, 4)
        self.assertEquals(bt.__findNode__(9).left.key, 5)
        self.assertEquals(bt.__findNode__(5).right.key, 7)
        bt.remove(16)
        self.assertEquals(bt.__findNode__(15).left.key, 11)
        self.assertEquals(bt.__findNode__(15).right.key, 17)
        self.assertEquals(bt.__findNode__(11).right.key, 14)

        

if __name__ == '__main__':
    unittest.main()
