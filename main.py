from flask import Flask
import requests


app = Flask(__name__)


@app.route("/weathercurrent/<lan>/<lat>")
def weathercurrent(lan, lat):
    link = """
          https://api.openweathermap.org/data/2.5/weather?lat=""" + str(lan) + """&lon=""" + str(lat) + """&appid=7ed4776295f2355723df6c8532184620"""
    r = requests.get(link)

    dataDict = r.json()

    # return dataDict

    dataDict = r.json()
    try:
        temp = dataDict["main"]["temp"]
        windSpeed = dataDict["wind"]["speed"]
        windDeg = dataDict["wind"]["deg"]
        #here return equations values
        return  {
                   "Temp":temp,
                   "windSpeed": windSpeed,
                   "windDeg": windDeg
              }
    # except:
    except:
        return ("Error")



if __name__ == "__main__":
    app.run(debug=True)

