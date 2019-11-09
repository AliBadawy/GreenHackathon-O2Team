from flask import Flask
import requests
import math
import operator


app = Flask(__name__)


@app.route("/weather")
def weathercurrent():
    city = "Alex"
    try:
        if city == "Alex":
            lat1Alex = 31.2
            lat2Alex = 31.6
            lat3Alex = 32
            lon1Alex = 29.7
            lon2Alex = 30
            lon3Alex = 30.1
            Alexandria = {
                "point1": [lat1Alex, lon1Alex],
                "point2": [lat2Alex, lon1Alex],
                "point3": [lat3Alex, lon1Alex],
                "point4": [lat1Alex, lon2Alex],
                "point5": [lat2Alex, lon2Alex],
                "point6": [lat3Alex, lon2Alex],
                "point7": [lat1Alex, lon3Alex],
                "point8": [lat2Alex, lon3Alex],
                "point9": [lat3Alex, lat3Alex]
            }
            results = {}
            for point in Alexandria.keys():
                link = """
                         https://api.openweathermap.org/data/2.5/weather?lat=""" + str(Alexandria[point][0]) + """&lon=""" + str( Alexandria[point][1]) + """&appid=7ed4776295f2355723df6c8532184620"""
                r = requests.get(link)
                dataDict = r.json()

                #Parsing the results
                temp = dataDict["main"]["temp"]
                windSpeed = dataDict["wind"]["speed"]
                windDeg = dataDict["wind"]["deg"]
               # here return equations values

                results[point] = {"Temp": temp, "windSpeed": windSpeed, "windDeg": windDeg}
            #    {"Temp": temp, "windSpeed": windSpeed, "windDeg": windDeg}

            #calcutlatin the formula
            t = {}
            for point in results.keys():
                t[point] = ((results[point]["windSpeed"]-results["point5"]["windSpeed"])*math.tan(results[point]["windDeg"]-results["point5"]["windDeg"]))/results[point]["Temp"]

            # For getting max value max(stats.items(), key=operator.itemgetter(1))[0]
            minimum = t[min(t.items(), key=operator.itemgetter(1))[0]]
            maximum = t[max(t.items(), key=operator.itemgetter(1))[0]]
            finalResult = {}

            for point in t.keys():
                finalResult[point] = 1 - (t[point] - minimum) / (maximum - minimum)
        return (finalResult)
            # return (5)
    except:
        return("Error")



if __name__ == "__main__":
    app.run(debug=True)

