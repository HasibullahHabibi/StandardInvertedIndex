class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTree:
    def __init__(self, t):
        self.t = t
        self.root = BTreeNode(t, True)

    def search(self, k, node=None):
        if node is None:
            node = self.root

        i = 0
        while i < len(node.keys) and k > node.keys[i]:
            i += 1

        if i < len(node.keys) and k == node.keys[i]:
            return node.keys[i]

        if node.leaf:
            return None
        return self.search(k, node.children[i])

    def insert(self, k):
        root = self.root
        if len(root.keys) == 2 * self.t - 1:
            new_node = BTreeNode(self.t, False)
            new_node.children.append(root)
            self.split_child(new_node, 0)
            self.root = new_node
            self._insert_non_full(new_node, k)
        else:
            self._insert_non_full(root, k)

    def _insert_non_full(self, node, k):
        i = len(node.keys) - 1

        if node.leaf:
            node.keys.append(None)
            while i >= 0 and k < node.keys[i]:
                node.keys[i+1] = node.keys[i]
                i -= 1
            node.keys[i+1] = k

        else:
            while i >= 0 and k < node.keys[i]:
                i -= 1
            i += 1

            if len(node.children[i].keys) == 2 * self.t - 1:
                self.split_child(node, i)
                if k > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], k)

    def split_child(self, parent, i):
        t = self.t
        y = parent.children[i]
        z = BTreeNode(t, y.leaf)

        parent.children.insert(i + 1, z)
        parent.keys.insert(i, y.keys[t - 1])

        z.keys = y.keys[t: (2 * t - 1)]
        y.keys = y.keys[0: t - 1]

        if not y.leaf:
            z.children = y.children[t:(2 * t)]
            y.children = y.children[0:t]

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        print("Level", level, "Keys:", node.keys)
        for child in node.children:
            self.print_tree(child, level + 1)
