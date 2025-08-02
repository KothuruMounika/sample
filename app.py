from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
#create templates folder=>index.html
def index():
    return render_template("index.html")
@app.route("/home")
def home():
    return "home page"
@app.route("/index1")
def index1():
    return "index1 page"
if __name__=="__main__":
    app.run(host='0.0.0.0',port=10000)