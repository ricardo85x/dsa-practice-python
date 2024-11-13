class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def lst_to_tree(lst) -> TreeNode: 
    if not lst:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in lst]
    for i, node in enumerate(nodes):
        if node:
            if 2 * i + 1 < len(nodes):
                node.left = nodes[2 * i + 1]
            if 2 * i + 2 < len(nodes):
                node.right = nodes[2 * i + 2]
    return nodes[0]