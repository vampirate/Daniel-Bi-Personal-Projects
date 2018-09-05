from flask import Flask, render_template
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


if __name__ == '__main__':
   app.run(debug=True)
