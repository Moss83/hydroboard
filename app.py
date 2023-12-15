from flask import Flask, jsonify, make_response
from hydro_func import k_means

app = Flask(__name__)

@app.route("/kmeans/<humedad>/<precipitacion>/<temperatura>/<viento>/<ffmc>/<dmc>/<dc>", methods=["GET"])
def kmeans(humedad, precipitacion, temperatura, viento, ffmc, dmc, dc):
    return make_response(jsonify(prediccion=str(k_means(temperatura, humedad, viento, precipitacion, ffmc, dmc, dc))), 200)

if __name__ == "__main__":
    app.run(debug=True, port=5000)