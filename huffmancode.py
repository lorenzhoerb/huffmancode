class Node:

    def __init__(self, alphabet, prob):
        self.left = None
        self.right = None
        self.prob = prob
        self.alphabet= alphabet

# init leaf_path
leaf_path = []
# init output object 
output = []

def gen_huffman(code):
    binary_tree = gen_binary_tree(code)
    get_leaf_paths(binary_tree)

    # sort output by probability
    sorted_output = sorted(output, key = lambda i: len(i['coding']))

    # print huffman codes
    for elem in sorted_output:
        prob = elem['prob']*100
        prob = "{:.2f}".format(prob) # round to two decimal points
        print('Alphabet: ' + elem['name'] + '\t Coding: ' + elem['coding'] + '\t\t Probability: ' + prob + '%')

# creates a binary tree from input data
def gen_binary_tree(codes):
    # init merging list
    working_list = []

    # init working_list with nodes
    for code in codes:
        node = Node(code['name'], code['prob'])
        working_list.append(node)

    while len(working_list) > 1:
        # sort nodes by prob
        working_list = sorted(working_list, key = lambda i: i.prob, reverse=True)

        # pop nodes with least prob
        node1 = working_list.pop()
        node2 = working_list.pop()
        # create new Node
        new_prob = node1.prob + node2.prob
        new_node = Node(None, new_prob)
        if node1.prob <= node2.prob:
            new_node.left = node1
            new_node.right = node2
        else:
            new_node.left = node2
            new_node.right = node1

        # add combined nodes to working_list
        working_list.append(new_node)

    return working_list[0] # returns root node

def get_leaf_paths(root):
    # if node is leafe
    if not root.left and not root.right:
        str_leaf_path = ''.join([str(x) for x in leaf_path]) # leaf path to string 
        code = {'name': root.alphabet, 'prob': root.prob, 'coding': str_leaf_path}
        output.append(code)
        return 

    if root.left:
        leaf_path.append(0)
        get_leaf_paths(root.left)
        leaf_path.pop()

    if root.right:
        leaf_path.append(1)
        get_leaf_paths(root.right) 
        leaf_path.pop()

if __name__ == '__main__':
    codes = [
        {'name':'r1', 'prob': 0.15},
        {'name':'r2', 'prob': 0.1},
        {'name':'r6', 'prob': 0.5},
        {'name':'r8', 'prob': 0.2},
        {'name':'r7', 'prob': 0.04},
        {'name':'r12', 'prob': 0.01},
    ]

    beta = [
        {'name':'β', 'prob': 0.32},
        {'name':'λ', 'prob': 0.28},
        {'name':'ε', 'prob': 0.19},
        {'name':'γ', 'prob': 0.11},
        {'name':'α', 'prob': 0.08},
        {'name':'σ', 'prob': 0.02},
    ]

    alpha = [
        {'name':'a', 'prob': 0.01},
        {'name':'b', 'prob': 0.09},
        {'name':'c', 'prob': 0.20},
        {'name':'d', 'prob': 0.03},
        {'name':'e', 'prob': 0.03},
        {'name':'f', 'prob': 0.03},
        {'name':'g', 'prob': 0.01},
        {'name':'h', 'prob': 0.20},
        {'name':'i', 'prob': 0.15},
        {'name':'j', 'prob': 0.15},
        {'name':'k', 'prob': 0.02},
        {'name':'l', 'prob': 0.08},
        {'name': 'p', 'prob': 0.04}
    ]
    gen_huffman(alpha)
