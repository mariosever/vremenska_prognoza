from flask import Flask, render_template
import requests

app = Flask(__name__)

# ovo je glavni dio aplikacije

@app.route("/", methods=["GET"])
def index():

    query = "Zagreb"
    unit = "metric"
    apikey = "ovdje ubaci svoj api ključ :-)"

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}&lang=hr".format(query, unit, apikey)

    data = requests.get(url=url)

    return render_template("index.html", data=data.json())




if __name__ == '__main__':
    app.run()


