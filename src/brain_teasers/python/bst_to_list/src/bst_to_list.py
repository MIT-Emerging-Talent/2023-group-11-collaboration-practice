
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bst_to_double_linked_list(root):
    def inorder_traversal(node):
        nonlocal prev, head

        if not node:
            return

        inorder_traversal(node.left)

        if prev is None:
            head = node
        else:
            prev.right = node
            node.left = prev

        prev = node

        inorder_traversal(node.right)

    if not root:
        return None

    head = None
    prev = None

    inorder_traversal(root)

    return head
