import CaboCha

def parsing(sentence):
    parser = CaboCha.Parser()
    tree = parser.parse(sentence)
    print(tree.toString(CaboCha.FORMAT_LATTICE))

if __name__ == "__main__":
    parsing("12行目において、変数Aはこの処理のために用意されている。関数Bは特に使われていない。")