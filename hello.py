from flask import Flask, render_template
import subprocess
from subprocess import call

app = Flask(__name__)

@app.route("/")
@app.route("/Home")
def home():
   return render_template("Home.html")

@app.route("/Info")
def myInfo():
   return render_template("Information.html")


@app.route("/Image")
def ImageIdentifier():
   return render_template("Image Identifier.html")

@app.route("/DogOrCat")
def DogOrCat():
   return render_template("DogOrCat.html")

@app.route("/getimageurl", methods = ['POST'])
def getimageurl():
    print("HEY")
    url = "https://i.ytimg.com/vi/SfLV8hD7zX4/maxresdefault.jpg"
    out = subprocess.check_output(["python", "static/cnn/cnn.py", url])
    print(out)
    return(out)


if __name__ == '__main__':
   app.run(debug=True)
