from flask import Flask, request, jsonify,render_template

app=Flask(__name__,template_folder='template')

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/greet", methods=["GET", "POST"])
def greet():
    name = request.args.get("name","world")
    splitName = name.split("/")
    print(splitName)
    return render_template("greet.html", name=name)


if __name__ == "__main__":
    app.run(debug = True)

