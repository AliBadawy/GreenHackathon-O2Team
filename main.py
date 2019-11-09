from flask import Flask
import requests


app = Flask(__name__)


@app.route("/weathercurrent/<lan>/<lat>")
def weathercurrent(lan, lat):
    link = """
         https://api.openweathermap.org/data/2.5/forecast/hourly?lat=""" + str(lan) + """&lon=""" + str(lat) + """&appid=efbcb9da9bd397d2be9c9b3213e70016
         """
    r = requests.get(link)

    dataDict = r.json()
    try:
        temp = dataDict["main"]["temp"]
        windSpeed = dataDict["wind"]["speed"]
        windDeg = dataDict["wind"]["deg"]
        #here return equations values
        return dataDict
    except:
        return ("Error")

@app.route("/weather4days/<lan>/<lat>")
def weather4days(lan, lat):
    link = """
         https://api.openweathermap.org/data/2.5/forecast/hourly?lat=""" + str(lan) + """&lon=""" + str(lat) + """&appid=efbcb9da9bd397d2be9c9b3213e70016
         """
    r = requests.get(link)

    dataDict = r.json()
    try:
        temp = []
        windSpeed = []
        windDeg = []
        for i in range(3):
            temp.append(dataDict["list"][i]["main"]["temp"])
            windSpeed.append(dataDict["list"][i]["wind"]["speed"])
            windDeg.append(dataDict["list"][i]["wind"]["deg"])
        #return formula resutls
        return dataDict
    except:
        return ("Error")

if __name__ == "__main__":
    app.run(debug=True)

