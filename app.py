from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
    return "Welcome to MRECW"
@app.route("/home")
def home():
    return "home page"
if __name__=="__main__":
    app.run(host='0.0.0.0',port=10000)