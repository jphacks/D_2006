import CaboCha
import Parsing


class Tree:
    def __init__(self):
        self.chunk_list = []
        self.token_list = []
        self.chunk_num = 0
        self.token_num = 0
    
    class Chunk:
        def __init__(self, string, num):
        #必要な変数の宣言、引数のデータを切り分けて各々の変数に振り分け
            #print(num, string)
            st = string.split(' ')
            #print(st)
            #print("num is: ", st[1].split('D')[0])
            self.chunk_id = int(num)
            self.link = st[1].split('D')[0]
            self.main_num = st[2][0]
            self.factional = st[2][2]
            self.score = st[3][0:-2]
            #self.print_all()

        def print_all(self):
        #全変数を表示
            print(self.chunk_id)
            print(self.link)
            print(self.main_num)
            print(self.factional)
            print(self.score)
            
    def add_chunk(self, string):
        #print('chunk_num', self.chunk_num)
        self.chunk_list.append(self.Chunk(string, self.chunk_num))
        self.chunk_num += 1
        self.token_num = 0
            
    class Token:
        def __init__(self, string, num):
        #必要な変数の宣言、引数のデータを切り分けて各々の変数に振り分け
            #print('str', num, string)
            st = string.split(',')
            #print(st)
            self.chunk_id = num
            self.text = st[0].split('\t')[0]
            self.surface = st[0].split('\t')[1]
            self.detail1 = st[1]
            self.detail2 = st[2]
            self.detail3 = st[3]
            self.inflected_from = st[4]
            self.inflected_type = st[5]
            self.original = st[6]
            #self.print_all()

        def print_all(self):
        #全変数を表示
            print(self.chunk_id)
            print(self.text)
            print(self.surface)
            print(self.detail1)
            print(self.detail2)
            print(self.detail3)
            print(self.inflected_from)
            print(self.inflected_type)
            print(self.original)

    def add_token(self, string):
        #print('token_num', self.token_num)
        self.token_list.append(self.Token(string, self.chunk_num-1))
        self.token_num += 1

