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
            #print(num, string)
            st = string.split(' ')
            #print(st)
            self.chunk_id = int(num)
            self.link = st[1][0]
            self.main_num = st[2][0]
            self.factional = st[2][2]
            self.score = st[3][0:-2]
            #self.print_all()

        def print_all(self):
            print(self.chunk_id)
            print(self.link)
            print(self.main_num)
            print(self.factional)
            print(self.score)
            
    def add_chunk(self, string):
        self.chunk_list.append(self.Chunk(string, self.chunk_num))
        self.chunk_num += 1
        self.token_num = 0
            
    class Token:
        def __init__(self, string, num):
            #print(num, string)
            st = string.split(',')
            print(st)
            self.chunk_id = num
            self.text = st[0].split('\t')[0]
            self.surface = st[0].split('\t')[1]
            self.detail1 = st[1]
            self.detail2 = st[2]
            self.detail3 = st[3]
            self.inflected_from = st[4]
            self.inflected_type = st[5]
            self.original = st[6]
            #self.pronunciation = st[7]
            self.print_all()

        def print_all(self):
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
        self.token_list.append(self.Token(string, self.token_num))
        self.token_num += 1

            
def virtual_server():   #サーバ側での動作をシュミレートしている
    dic_file = open('e-words2.txt')    #マッチングファイルの読み込み
    res_file = open('parse_result.txt')
    sentence = virtual_input()  #文字の受信

    tr = Tree()     #解析結果ファイルを項目ごとにTreeクラスにまとめる
    for res in res_file:
        if res[0:3] == 'EOS':   #ファイルの終端を検知
            break
        elif res[0] == '*':     #新しいchunkを追加
            tr.add_chunk(res[2:])
        else:
            tr.add_token(res)   #新しい単語を追加

    nouns = []  #名詞の単語を集める
    
    
    matching(res_file, dic_file)       #マッチング関数の実行
    dic_file.close()               #ファイルのクローズ
    res_file.close()


def virtual_input():    #サーバー側での文字の受信をシュミレートしている
    return "アジャイル開発はエンジニアを幸せにするためにある。"   #受信した文字を変えす


def matching(result_file, matching_file):  #マッチング処理
    pass
            

if __name__ == "__main__":
    virtual_server()
    