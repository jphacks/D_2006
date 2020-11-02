import CaboCha

def parsing(sentence):
    parser = CaboCha.Parser()
    tree = parser.parse(sentence)
    result2 = tree.toString(CaboCha.FORMAT_TREE)
    result = tree.toString(CaboCha.FORMAT_LATTICE)
    
    with open('parse_result.txt', mode='w')as f:
        f.write(result)
        
    with open('parse_result2.txt', mode='w')as f2:
        f2.write(result2)

if __name__ == "__main__":
    print(parsing("12行目において、変数Aはこの処理のために用意されている。アジャイル開発を行っている。"))
