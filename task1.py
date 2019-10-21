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
t = Tree('*', [Tree('1'),
               Tree('2'),
               Tree('+', [Tree('3'),
                          Tree('4')])])

def calculate(t):
    value = 0.0
    if t.name == '+':
        for i in range(len(t.children)):
            value += check_value(t.children[i])
    if t.name == '-':
        value += check_value(t.children[0])
        for i in range(1, len(t.children)):
            value -= check_value(t.children[i])
    if t.name == '*':
        if value == 0:
            value = check_value(t.children[0])
        else:
            value *= check_value(t.children[0])
        for i in range(1, len(t.children)):
            value *= check_value(t.children[i])
    if t.name == '/':
        if value == 0:
            value = check_value(t.children[0])
        else:
            value *= check_value(t.children[0])
        for i in range(len(t.children)):
            value /= check_value(t.children[i])

    print(value)
    return value

def check_value(t):
    if t.name in('+', '-', '*', '/'):
        return calculate(t)
    else:
        return float(t.name)

value = calculate(t)