from flask import Flask,request,jsonify
from weather import Weather
application  = Flask(__name__)

@application.route("/weather/getWeatherInfo/<city>")
def getWeather(city):
    #city = request.args.get("city",default="Istanbul",type = str)    
    data = Weather().getInfo(city=city)

    return data
if __name__=="__main__":
    application .run()