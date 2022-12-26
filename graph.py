import numpy as np
from bigtree import Node, print_tree, prune_tree
from utils import reduksi_matrix


class graph:

    gdict: dict

    def __init__(self, gdict: dict = None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    def get_vertex(self) -> list:
        return list(self.gdict.keys())

    def get_edges(self, node: str) -> list:
        try:
            return list(self.gdict.get(node))
        except:
            return None

    def get_length(self, src: str, dst: str) -> dict:
        try:
            return self.gdict.get(src).get(dst)
        except:
            return None

    def list_to_matrix(self, case: list) -> list:
        size = len(case)
        arr = [[[] for _ in range(size)] for _ in range(size)]
        for i in range(size):
            for j in range(size):
                arr[i][j] = self.get_length(case[i], case[j])
        return arr

    def bnb_tree(self, lokasi: list, showStep: bool = False) -> None:
        vertex = lokasi.copy()
        if 'pintu' not in vertex:
            vertex.insert(0, 'pintu')
        if 'kasir' not in vertex:
            vertex.append('kasir')
        matrix = self.list_to_matrix(vertex)
        reduce_matrix, bound = reduksi_matrix(matrix)
        tree = Node("root", bound=bound, matrix=matrix)
        step = []
        step.append(Node('pintu', idx=0, bound=bound, visited=[], parent=tree))
        queue = []
        t = 1

        while True:
            c_node = step.pop()
            c_idx = c_node.get_attr("idx")
            c_bound = c_node.get_attr("bound")
            c_visited = c_node.get_attr("visited").copy()

            c_visited.append(c_idx)

            unvisited = [vertex.index(
                xx) for xx in lokasi if vertex.index(xx) not in c_visited]
            for x in [xx for xx in unvisited if xx not in c_visited]:

                prev_val = reduce_matrix[c_idx][x]

                if prev_val is None:
                    prev_val = 0

                Node(vertex[x], idx=x, bound=c_bound+prev_val,
                     visited=c_visited.copy(), parent=c_node)

            if len(c_node.children) < 1:
                Node('kasir', idx=vertex.index('kasir'), bound=c_bound,
                     visited=c_visited.copy(), parent=c_node)
                break

            c_children = [x for x in c_node.children]
            queue = sorted(np.concatenate((queue, c_children)),
                           key=lambda x: x.get_attr("bound"))
            step.append(queue.pop(0))
            if showStep:
                print("Step ", t, ":")
                print_tree(tree, attr_list=["bound"])
                print("\n")
                t += 1
        print_tree(prune_tree(tree, 'kasir'), attr_list=["bound"])
