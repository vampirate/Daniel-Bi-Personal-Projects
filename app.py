from flask import Flask, render_template, request, jsonify
import subprocess, logging, sys
from subprocess import call


app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@app.route("/")
@app.route("/Home")
def home():
   return render_template("Home.html", title = "Home Page", active = "Home")

@app.route("/Info")
def myInfo():
   return render_template("Information.html", title = "My Info", active = "Info")

@app.route("/Image")
def ImageIdentifier():
   return render_template("Image Identifier.html", title = "Image Identifier", active = "Image")

@app.route("/DogOrCat")
def DogOrCat():
   return render_template("DogOrCat.html", title = "Dog or Cat?", active = "DogOrCat")

@app.route("/DogOrCatStart", methods = ['POST'])
def DogOrCatStart():
    url = request.form['imageurl']
    ans = subprocess.check_output(["python", "static/cnn/dogcat.py", url])
    return ans.decode("utf-8")

@app.route("/Kmeans")
def Kmeans():
    return render_template("K-Means.html", title="K-means Clustering", active="Kmeans")

@app.route("/KmeansStart", methods = ['POST'])
def KmeansStart():
    k = request.form["k"]
    n = request.form["n"]
    r = request.form["r"]
    bokehDiv = subprocess.check_output(["python", "static/kmeans/kmeans.py", k, n, r])
    return bokehDiv

@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

if __name__ == '__main__':
   app.run(debug=True)
