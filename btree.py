import unittest
# # Assignment: Binary Tree

# Write a binary tree class that has the following methods:

# 1. `set(key, value)` stores a key=value pair to the tree in the appropriate spot.
# 1. `get(key)` returns the value stored with the given key.  If the key does not exist, null/None should be returned.
# 1. `remove(key)` removes the node with the given key from the tree.  If the key does not exist, it should simply return (no error).
# 1. `walk_dfs_inorder()` iterates through the nodes of the tree in depth-first-search "inorder" order.
# 1. `walk_dfs_preorder()` iterates through the nodes of the tree in depth-first-search "preorder" order.
# 1. `walk_dfs_postorder()` iterates through the nodes of the tree in depth-first-search "postorder" order.
# 1. `walk_bfs()` iterates through the nodes of the tree in breadth-first-search order.
# 1. `debug_print()` prints a graphical representation of the tree. See below for more information.