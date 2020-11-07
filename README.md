# デダック De:Duck

<img src="/readme_img/duck.png">

## 目次
1. [チーム名](#anchor1)
1. [製作背景](#anchor2)
1. [使い方](#anchor3)
1. [リンク](#anchor4)
1. [特徴](#anchor5)
1. [解決できること](#anchor6)
1. [今後の展望](#anchor7)
1. [注力したこと](#anchor8)
1. [開発技術](#anchor9)

<a id="anchor1"></a>
## チーム名
### チームメンバー
- 中尾龍矢　　　　　 :アルゴリズム担当
- 伊地知翔也　　　　 :UI兼サーバー構築
- パニアグアカルロス :UI担当

## 製品概要
### Debug × Tech
<img src="/readme_img/slide-1.png">

<a id="anchor2"></a>
### 製作背景
以前、友人にプログラムの相談を持ち掛けた際、うまく説明できず、なかなか解決に至らなかった経験があります。  
これをきっかけに「強化版ラバーダック・デバッグを作ってみたらどうだろう」と思い、開発に至りました。  
「ラバーダック・デバッグ」とはソフトウェア工学の一つの手法で、ゴム製アヒル人形にコードの説明を一行ずつを行い、その過程で解決策を得るというものです。  
この手法のメリットは、プログラマが自身のコードについて、達成したい目的と意図を言語化する過程にあります。（アヒル人形をプログラム初心者として捉え、）相手が正しく理解できるように様々な表現や着眼点を模索することで、新たな解決策と深い理解へ繋がることができます。  
本製品は、ユーザが話したアルゴリズムの動作や変数、関数といった関係をAIが解析し、わかりやすく表示します。これにより、理解を助けるとともに、意図していた説明との食い違いや、わかりずらい抽象的な単語を避け、わかりやすい説明と明快な理解を促します。  
<a id="anchor3"></a>
### 使い方
**1. 「開始ボタン」を押して話そう**

<img src="/readme_img/slide1.png">

**2. 話終わったら「終了ボタン」を押そう**

<img src="/readme_img/slide2.png">

**3. 右下の「送信ボタン」で解析開始**

<img src="/readme_img/slide3.png">

**4. 結果が表示させる**

<img src="/readme_img/slide4.png">


<a id="anchor4"></a>
### リンク
<a href="http://jphacks-2020.app.idichi.tk/#"> デダックのデモサイトはこちらです （Android/Desktop番Chromeのみ対応）</a>）
<a id="anchor5"></a>
### 特長
#### 1. 特長1  
音声での入力（説明）の中で、抽象的、複雑な単語（主に技術用語）を検知し、その部分の具体的な説明を推奨する。
#### 2. 特長2
実際にメモを取ることなく、画面と常に向かい合って作業ができるので、スムーズに説明と考察を繰り返せる。
#### 3. 特長3
入力された説明をAIで解析し、自動的に要点をかいつまみ表示する。

<a id="anchor6"></a>
### 解決出来ること
<a href="https://ja.wikipedia.org/wiki/%E3%83%A9%E3%83%90%E3%83%BC%E3%83%80%E3%83%83%E3%82%AF%E3%83%BB%E3%83%87%E3%83%90%E3%83%83%E3%82%B0"> 「ラバーダック・デバッグ」 </a>
特徴1の機能によって、再度説明をしたときに理解のしやすい説明になり、利用者を深い理解に誘導しやすくなります。
また、特徴3の機能によってユーザの認識と、実際に話した説明が食い違いを見つけやすくする。また、説明はできるが具体的にどんな実装をすればよいのかを納得しきれていないときに、判断の指標としてリスト化しておけます。

<a id="anchor7"></a>
### 今後の展望
- 要点を抽出する処理において、正確な文節の親子関係を推測する事が技術的に間に合わなかったこと
- 音声認識APIがchrome（Android/desktop番）のみしか対応していないので、対応させたい。
<a id="anchor8"></a>
### 注力したこと
- 利用者が入力した音声データから複雑な単語を抽出する機能
- チャット風のUIに仕上げたことで親密感を上げたこと
- Intro.jsを導入したことによりチュートリアルを実装したこと
- 自然言語処理（ユーザが話した言葉を解析する処理）

<a id="anchor9"></a>
## 開発技術
### 活用した技術
#### フレームワーク・ライブラリ・モジュール
- さくらインタネットサーバー
- CaboCha/南瓜
- MeCab
- Flask
- intro.js
- jQuery

<img src="/readme_img/slide5.png">

### 独自技術
#### ハッカソンで開発した独自機能・技術
- 利用者が入力した音声データから複雑な単語、伝えたい要点を抽出する機能

#### 製品に取り入れた研究内容
 自然言語処理の勉強と独自研究（CaboChaから送られてくる係り受けについて、親子関係の推定）
