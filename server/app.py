from flask import Flask,render_template,abort
import sys,os

from flask import request,Response
from flask_cors import CORS
from flask.helpers import make_response
app=Flask(__name__,static_url_path="/")
CORS(app)



@app.route("/")
def root():
    return render_template("index.html")

import sys
sys.path.append("../")
from algorithm.いじったらだめ import Matching

# import algorithm.いじったらだめ.Matching
'''
input
{
    analyze_text:str
}

return 
{
    difficult_words:{
        {words},
        {words},...
    }
    analyzed_text:str{
      {sentence},...
    }
}
'''
import json
@app.route("/analyze",methods=["POST"])
def anal():
    message = request.get_json()
    text=message["analyze_text"]
   
       
    print("show-->",text)
    print("show end")
    ## Matching()
    #先に難しい単語を抽出した文を返す(string型)
    #二個目に要点をまとめた文を返す([str])
    words,text=Matching.virtual_server(text)
    if len(words)==0:
     words.append(["ありませんでした"])
    if len(text)==0:
      text.append("解析できませんでした")

    test={"analyzed_text":text,"difficult_words":words}
    return json.dumps(test),200
    
if __name__ == "__main__":
    print(app.url_map)
    app.run()
