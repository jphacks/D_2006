import CaboCha

def parsing(sentence):
    parser = CaboCha.Parser()
    tree = parser.parse(sentence)
    result_lattice = tree.toString(CaboCha.FORMAT_LATTICE)
    #print(result_lattice)
    #print(tree.toString(CaboCha.FORMAT_TREE))

    return result_lattice

if __name__ == "__main__":
    parsing("12行目において、変数Aはこの処理のために用意されている。アジャイル開発を行っている。")