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
    combine_num, combine_str, combine_list, count = -2, "", [], -1
    nouns = []  #名詞の単語を集める
    for i, word in enumerate(tr.token_list):  #単語集を走破
        if word.surface == "名詞":  #名詞かどうかを判定
            count += 1  #カウンタを加算
            if i == combine_num+1:  #一つ前のcombine_numと一致(前回検知した名詞から連続している)
                if combine_str == '':   #一つ前の名詞を追加する
                    combine_str += nouns[-1][0]     #名詞を結合
                    combine_list.append(count-1)    #番号を保存(nounsリスト内のインデックスとなる)
                combine_str += word.text    #文字列を結合
                combine_list.append(count)  #結合した文字のインデックスを保存
                #print('conbine')
            elif combine_str != '':     #連続していた名詞列が途切れたら
                nouns.append([combine_str, combine_list])   #それまで連続していた名詞達を結合した物をリストに保存
                #print(combine_str)
                combine_str = ''    #結合文字列を初期化
                combine_list = []   #結合も文字列リストを初期化
                
            combine_num = i     #nounsリスト内でのインデックスを保存
            nouns.append([word.text, [count]])   #名詞ならリストに追加
            #print([word.text, count])
            
    if combine_str != '':   #最後に結合文字列リスト内に残っている結合文字列を保存
        nouns.append([combine_str, [combine_list]])
        #print(combine_str)
        
    #print(nouns)

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


def calc_rate(match, param):   #評価値を計算する
    rate = 0.0
    for i in range(match):
        rate += 1/(param*(i+1))     #分数関数状にスコアがたまりにくくなる
        #print("rate: ", rate)
    return rate

    
def matching(nouns, dic_file):  #マッチング処理
    detection, Severity = [], 2     #detection:検知された名詞の中でも特に難しいと判断された文字列のリスト, Severity: 名詞の閾値調整に使う
    data = dic_file.read()  #分けられていない辞書データ
    data_sep = data.split()     #分けられた辞書リスト
    
    for word in nouns:  #検知された全ての名詞について調べる
        judge_score = float(len(word[1]))   #閾値の設定
        #print(word[0], judge_score)
        score = 0.0     #スコアの初期化
        if judge_score > 1:     #もしword[0]が結合後の文字列だったら
            for index in word[1]:   #全ての結合文字列達の出現個数によって評価値を計算する
                #score += data.count(nouns[index][0])
                score += calc_rate(data.count(nouns[index][0]), Severity)   #出現数が多いほど評価が高い
                #print (calc_rate(data.count(nouns[index][0]), Severity))
        if word[0] in data_sep:     #もしword[0]がそのまま出現したら
            score += judge_score    #スコアが一気に閾値まで上がる
        if score >= judge_score:    #閾値を超えていたら
            detection.append(word[0])   #リストに追加
            
    return detection


if __name__ == "__main__":
    virtual_server()
    