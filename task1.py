class Tree(object):
    "Generic tree node."
    def __init__(self, name='root', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self):
        return self.name

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)
#    *
#   /|\
#  1 2 +
#     / \
#    3   4


root_node = Tree('*', [Tree('1'),
                       Tree('2'),
                       Tree('+', [Tree('3'),
                                  Tree('4')])])

def calculate(root_node):
    value = 0.0
    if root_node.name == '+':
        for i in range(len(root_node.children)):
            value += check_value(root_node.children[i])
    if root_node.name == '-':
        value += check_value(root_node.children[0])
        for i in range(1, len(root_node.children)):
            value -= check_value(root_node.children[i])
    if root_node.name == '*':
        if value == 0:
            value = check_value(root_node.children[0])
        else:
            value *= check_value(root_node.children[0])
        for i in range(1, len(root_node.children)):
            value *= check_value(root_node.children[i])
    if root_node.name == '/':
        if value == 0:
            value = check_value(root_node.children[0])
        else:
            value *= check_value(root_node.children[0])
        for i in range(len(root_node.children)):
            value /= check_value(root_node.children[i])

    return value


def check_value(root_node):
    if root_node.name in('+', '-', '*', '/'):
        return calculate(root_node)
    else:
        return float(root_node.name)

value = calculate(root_node)