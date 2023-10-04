from flask import Flask
from hydro_func import k_means

app = Flask(__name__)

@app.route("/kmeans/<humedad>/<precipitacion>", methods=["POST"])
def kmeans(humedad, precipitacion):
    return str(k_means(humedad, precipitacion))