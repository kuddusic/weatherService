import json
import urllib2


class Weather():
    def __init__(self):
        self.weatherBaseUrl = "http://api.openweathermap.org/data/2.5/"
        self.appkey = "3d049d48e11ad8bf9a8a7d01c66135aa"

    def getInfo(self, city="Istanbul", apptype="weather"):
        # type: (object, object) -> object
        if apptype == "weather":
            application = "weather"
            if city.isalpha():
                querykey = "q=%s" % city
            else:  # it meant id is supplied
                querykey = "id=%s" % city
            finalUrl = "%s%s?APPID=%s&%s" % (self.weatherBaseUrl, application, self.appkey, querykey)
            jsondata, errorMessage = self.getDataAsJSON(finalUrl)
            retValue = {}
            if errorMessage is not None:
                retValue["error"] = errorMessage
                return json.dumps(retValue)
            else:
                temp = int(jsondata["main"]["temp"] - 273.15)
                retValue["error"] = "0"
                retValue["temp"] = temp
            return json.dumps(retValue)

    def getDataAsJSON(self, url):
        error_message = None
        jsondata = None
        try:
            response = urllib2.urlopen(url)
            data = response.read()
        except urllib2.HTTPError as e:
            error_message = "Exception:%s,%s" % (e.code, e.read())
            return (jsondata, error_message)
        except Exception as e:
            error_message = "URLLib Exception:%s" % str(e)
            return (jsondata, error_message)
        try:
            jsondata = json.loads(data)
        except ValueError as e:
            error_message = "JSON Decode Error: %s on pos:%d, col:%d" % (e.msg, e.pos, e.colno)
        if jsondata["cod"] != 200:
            error_message = jsondata["message"]
        return (jsondata, error_message)


if __name__ == "__main__":
    print(Weather().getInfo())
