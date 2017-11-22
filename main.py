from btree import BinaryTree



# 1. Create the tree by storing following key=value pairs:
#         c = C
#         h = H
#         a = A
#         e = E
#         f = F
#         d = D
#         b = B
#         j = J
#         g = G
#         i = I
#         k = K
bt = BinaryTree()
print('Initial Tree:')
bt.__set__('c','C')
bt.__set__('h','H')
bt.__set__('a','A')
bt.__set__('e','E')
bt.__set__('f','F')
bt.__set__('d','D')
bt.__set__('b','B')
bt.__set__('j','J')
bt.__set__('g','G')
bt.__set__('i','I')
bt.__set__('k','K')

# 2. Print the tree with `debug_print()`.
bt.debug_print()

print('\nLookups:')
# 3. Print the value with key = `f`.
print(bt.__findNode__('f').value)

# 4. Print the value with key = `b`.
print(bt.__findNode__('b').value)

# 5. Print the value with key = `i`.
print(bt.__findNode__('i').value)

# 6. Walk the tree in `BFS` order and print each value.
print('\nBFS:')
bfs = bt.walk_bfs()
for b in bfs:
    print(str(b.value))

# 7. Walk the tree in `DFS preorder` order and print each value.
print('\nDFS preorder:')
bt.walk_dfs_preorder(bt.root)

# 8. Walk the tree in `DFS inorder` order and print each value.
print('\nDFS inorder:')
bt.walk_dfs_inorder(bt.root)

# 9. Walk the tree in `DFS postorder` and print each value.
print('\nDFS postorder:')
bt.walk_dfs_postorder(bt.root)

# 10. Remove the value with key = `b`.
print('\nRemove b:')
bt.remove('b')
# 11. Print the tree with `debug_print()`.
bt.debug_print()
# 12. Remove the value with key = `f`.
print('\nRemove f:')
bt.remove('f')
# 13. Print the tree with `debug_print()`.
bt.debug_print()
# 14. Remove the value with key = `h`.
print('\nRemove h:')
bt.remove('h')
# 15. Print the tree with `debug_print()`.
bt.debug_print()

