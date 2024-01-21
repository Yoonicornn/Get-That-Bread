from flask import Flask, request, jsonify,render_template
from LinearRegression import predict_price
from app import input_to_index_bread, input_to_index_sp

app=Flask(__name__,template_folder='template')

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/greet", methods=["GET", "POST"])
def greet():
    name = request.args.get("name","world")
    splitName = name.split("/")
    year = int(splitName[0])  
    month = int(splitName[1])
    print(year)
    print(month)

    name= predict_price("WhiteBread.csv",year,month)
    name=round(name[0],2)
    print(name)
    
    return render_template("greet.html", name=name)


if __name__ == "__main__":
    app.run(debug = True)

