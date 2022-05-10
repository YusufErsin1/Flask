from flask import Flask,render_template

app=Flask(__name__)
@app.route("/")
def index():
    article=dict()
    article["title"]="Deneme"
    article["body"]="Kimi"
    article["author"]="everbody"
    return render_template("index.html",article=article)

if __name__ == "__main__":
    app.run(debug=True)