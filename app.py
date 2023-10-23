from flask import Flask , render_template, request
import requests 

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("QR_Code.html")

@app.route("/",methods = ['POST' , "GET"])
def get_QRCode():
    
    param = {
        'q':request.get(),
        
        }
    response = requests.get()
    data =  requests.get()
    return f"data : {data}"

if __name__ == '__main__':
    app.run(host= "0.0.0.0")


