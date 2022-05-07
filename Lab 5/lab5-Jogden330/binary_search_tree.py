from queue_array import Queue


class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:

    def __init__(self):  # Returns empty BST
        self.root = None

    def is_empty(self):  # returns True if tree is empty, else False
        if self.root is None:
            return True
        else:
            return False

    # returns True if key is in a node of the tree, else False
    def search(self, key):
        if self.root is None:
            return False
        else:
            return self.search_rec(key, self.root)

    def search_rec(self, key, node):
        if node.key == key:
            return True
        elif key < node.key:
            if node.left is None:
                return False
            else:
                return self.search_rec(key, node.left)
        elif key > node.key:
            if node.right is None:
                return False
            else:
                return self.search_rec(key, node.right)


    # inserts new node w/ key and data
    # If an item with the given key is already in the BST,
    # the data in the tree will be replaced with the new data
    def insert(self, key, data=None):
        if self.is_empty():
            self.root = TreeNode(key, data)
        else:
            self.insert_rec(key, data, self.root)

    def insert_rec(self, key, data, node):
        if node.key == key:
            node.data = data
        elif key < node.key:
            if node.left is None:
                node.left = TreeNode(key, data)
            else:
                self.insert_rec(key, data, node.left)
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key, data)
            else:
                self.insert_rec(key, data, node.right)

    # returns a tuple with min key and data in the BST
    # returns None if the tree is empty
    def find_min(self):
        if self.root is None:
            return None
        else:
            return self.find_min_rec(self.root)

    def find_min_rec(self, node):
        if node.left is None:
            return (node.key, node.data)
        else:
            return self.find_min_rec(node.left)

    # returns a tuple with max key and data in the BST
    # returns None if the tree is empty
    def find_max(self):
        if self.root is None:
            return None
        else:
            return self.find_max_rec(self.root)

    def find_max_rec(self, node):
        if node.right is None:
            return (node.key, node.data)
        else:
            return self.find_max_rec(node.right)

    def tree_height(self):  # return the height of the tree
        if self.root == None:
            return None
        return self.tree_height_rec(self.root) - 1

    def tree_height_rec(self, node):
        if node is None:
            return 0
        return max(self.tree_height_rec(node.left), self.tree_height_rec(node.right)) +1
    # return Python list of BST keys representing in-order traversal of BST
    def inorder_list(self):
        return self.inorder_list_rec(self.root)

    def inorder_list_rec(self, node):
        if node is None:
            return []
        return self.inorder_list_rec(node.left) + [node.key] + self.inorder_list_rec(node.right)

    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        return self.preorder_list_rec(self.root)

    def preorder_list_rec(self, node):
        if node is None:
            return []
        return [node.key] + self.preorder_list_rec(node.left) + self.preorder_list_rec(node.right)

    # return Python list of BST keys representing level-order traversal of BST
    # You MUST use your queue_array data structure from lab 3 to implement this method
    def level_order_list(self):
        q = Queue(25000)  # Don't change this!
        list_level = []
        if self.root is None:
            return list_level
        q.enqueue(self.root)
        while not q.is_empty():
             node = q.dequeue()
             list_level = list_level + [node.key]
             if node.left is not None:
                 q.enqueue(node.left)
             if node.right is not None:
                 q.enqueue(node.right)
        return list_level