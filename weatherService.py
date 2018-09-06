from flask import Flask,request,jsonify
from weather import Weather
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/weather/getWeatherInfo/<city>")
def getWeather(city):
    #city = request.args.get("city",default="Istanbul",type = str)    
    data = Weather().getInfo(city=city)

    return data
