from flask import Flask
from flask import request
from flask import render_template, send_file
coconut = Flask(__name__)

@coconut.route("/")
def main():
    return render_template("index.html")
@coconut.route("/coconut.png")
def get_image():
    filename='coconut.png'
    return send_file(filename,mimetype='image/png')
   
if __name__ == "__main__":
    coconut.run(host="0.0.0.0", port=8080)