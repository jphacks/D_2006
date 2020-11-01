import CaboCha

def parsing(sentence):
    parser = CaboCha.Parser()
    tree = parser.parse(sentence)
    result = tree.toString(CaboCha.FORMAT_LATTICE)
    
    return result
#    with open('parse_result.txt', mode='w')as f:
#        f.write(result)

if __name__ == "__main__":
    print(parsing("12行目において、変数Aはこの処理のために用意されている。アジャイル開発を行っている。"))
