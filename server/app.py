from flask import Flask,render_template,abort
import sys,os

from flask import request,Response
app=Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

if __name__ == "__main__":
    # app.static_folder="static"
    app.static_url_path=""
    app.run(
         host="0.0.0.0",port=5000,debug=True
    )
