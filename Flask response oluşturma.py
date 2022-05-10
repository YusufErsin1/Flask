from flask import Flask

app=Flask(__name__)
@app.route("/")
def index():
    return "Ana sayfa"

@app.route("/about")
def about():
    return "Hakkımda"

if __name__ == "__main__":
    app.run(debug=True)