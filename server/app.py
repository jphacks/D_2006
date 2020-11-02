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
    test={"analed_text":text}
    return json.dumps(test),200
    
if __name__ == "__main__":
    print(app.url_map)
    app.run()
