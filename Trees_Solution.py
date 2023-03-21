#Problem 1: Binary Search Tree 
#This function is complete, use as a reference only if you have completed the solution or are stuck. 

class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None 

def insert_node(root, value):
    if root is None:
        root = Node(value)
    elif value < root.value:
        root.left = insert_node(root.left, value)
    else: root.right = insert_node(root.right, value)
    return root 


#Test Problem 1: Binary Search Tree 

root = Node(5)
insert_node(root, 2)
insert_node(root, 20)
assert root.value == 5
assert root.left.value == 2
assert root.right.value == 20



#Problem 2: Balanced Binary Search Tree
#This function is complete, use as a reference only if you have completed the solution or are stuck. 

class CreateTree(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sort_array(numbers):
    if not numbers: 
        return None
    mid_value = len(numbers)//2
    node = CreateTree(numbers[mid_value])
    node.left = sort_array(numbers[:mid_value])
    node.right = sort_array(numbers[mid_value+1:])
    return node

def orderNodes(node):
    if not node:
        return 
    print(node.value)
    orderNodes(node.left)
    orderNodes(node.right)

result = sort_array([1, 2, 3, 4, 5])
orderNodes(result)


#Test Problem 2: Balanced Binary Search Tree

numbers = [4, 2, 5, 1, 3]
result = sort_array(numbers)
assert result.value == 3
assert result.left.value == 2
assert result.right.value == 5
assert result.left.left.value == 1
assert result.left.right.value == 4


