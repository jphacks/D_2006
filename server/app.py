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

from ..algorithm.いじったらだめ import Matching
# import algorithm.いじったらだめ.Matching
'''
input
{
    anal_text:str
}

return 
{
    analed_text:str
}
'''
import json
@app.route("/anal",methods=["POST"])
def anal():
    message = request.get_json()
    text=message["anal_text"]
    # todo anal

    ans=Matching.virtual_server(text)
    ans=ans.replace("{","<strong>")
    ans=ans.replace("}","</strong>")

    test={"analed_text":ans}
    return json.dumps(test),200
    
if __name__ == "__main__":
    print(app.url_map)
    app.run()
