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
            self.chunk_id = int(num)
            self.link = st[1][0]
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
        self.chunk_list.append(self.Chunk(string, self.chunk_num))
        self.chunk_num += 1
        self.token_num = 0
            
    class Token:
        def __init__(self, string, num):
        #必要な変数の宣言、引数のデータを切り分けて各々の変数に振り分け
            #print(num, string)
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
        self.token_list.append(self.Token(string, self.token_num))
        self.token_num += 1

            
def virtual_server():   #サーバ側での動作をシュミレートしている

#--------------------------------------------
#必要なデータの収集
#--------------------------------------------
    sentence = virtual_input()  #文字の受信
    Parsing.parsing(sentence)   #文書の解析を実行
    dic_file = open('e-words2.txt')    #マッチングファイルの読み込み

    
#--------------------------------------------
#解析結果をまとめ上げる
#--------------------------------------------
    res_file = open('parse_result.txt')     #解析結果ファイルの読み込み
    tr = Tree()     #解析結果ファイルを項目ごとにTreeクラスにまとめる
    for res in res_file:
        if res[0:3] == 'EOS':   #ファイルの終端を検知
            break
        elif res[0] == '*':     #新しいchunkを追加
            tr.add_chunk(res[2:])
        else:
            tr.add_token(res)   #新しい単語を追加
    res_file.close()    #解析が終わったのでファイルは不要


#--------------------------------------------
#まとめ上げられた物から必要な物のみ取り出す
#--------------------------------------------
    combine_num, combine_str = -2, ""
    nouns = []  #名詞の単語を集める
    for i, word in enumerate(tr.token_list):  #単語集を走破
        if word.surface == "名詞":  #名詞かどうかを判定
            if i == combine_num+1:
                if combine_str == '':
                    combine_str += nouns[-1]
                combine_str += word.text
                #print('conbine')
            elif combine_str != '':
                nouns.append(combine_str)
                #print(combine_str)
                combine_str = ''
                
            combine_num = i
            nouns.append(word.text)   #名詞ならリストに追加
            #print([word.text, i])
            
    if combine_str != '':
        nouns.append(combine_str)
        print(combine_str)
        
    print(nouns)

#--------------------------------------------
#IT用語集と照合
#--------------------------------------------
    detection = matching(nouns, dic_file)       #マッチング関数の実行
    print(detection)

#--------------------------------------------
#後掃除
#--------------------------------------------
    dic_file.close()               #ファイルのクローズ


def virtual_input():    #サーバー側での文字の受信をシュミレートしている
    return "ハードウェアについては、演算処理装置の高速化・搭載量の拡大、演算時のメモリ搭載量の大容量化・高速化、演算処理装置間でのメモリ共有方式が特徴的である。他にベクトル計算に特有の演算処理装置を備える等、取り扱われる演算に特有のハードウエア方式が採用されることがある。 また高い計算能力は演算処理を担う電子回路の大規模・高速なスイッチング動作により実現されるため、大量の電力消費と発熱に対応した電源設備、排熱・冷却機構が必要である。abstractクラス"
    #return "アジャイル開発はエンジニアを幸せにするためにある。"   #受信した文字を変えす


def matching(nouns, dic_file):  #マッチング処理
    detection = []
    data = dic_file.read()
    data_sep = data.split()
    for word in nouns:
        if(word in data_sep):
            detection.append(word)
            
    return detection
            

if __name__ == "__main__":
    virtual_server()
    