from flask import Flask, request, jsonify,render_template
from LinearRegression import predict_price
from app import input_to_index_bread, input_to_index_sp

app=Flask(__name__,template_folder='template')

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/greet", methods=["GET", "POST"])
def greet():
   
    savings=request.args.get("savings")
    date_month=request.args.get("month")
    futur_year=request.args.get("year")
    bread_year=request.args.get("bread_year")
    bread_month=request.args.get("bread_month")
    
    bread_year=int(bread_year)
    bread_month=int(bread_month)
   
    futur_year=int(futur_year)
    savings=int(savings)
    date_month=int(date_month)
   
    
    
    
    print(savings)
    print(date_month)
    print(futur_year)

    inflation= predict_price("WhiteBread.csv",bread_year,bread_month)

    investment=predict_price("S&P500.csv",futur_year,date_month)
    total=(savings/4839.81)*investment
    print(total)
    total=total[0]
    total=round(total,2)

    inflation = inflation[0]
    inflation = round(inflation,2)
    
    percentage_bread = ((inflation - 4.22)/4.22) * 100
    percentage_bread = round(percentage_bread,2)
    percentage_investment= ((total-1000)/1000)*100
    percentage_investment=round(percentage_investment,2)
    
    print(investment)
    
    return render_template("greet.html", inflation=inflation,bread_year=bread_year, percentage_bread=percentage_bread,savings=savings,date_month=date_month, investment=investment,total=total, percentage_investment=percentage_investment)


if __name__ == "__main__":
    app.run(debug = True)

