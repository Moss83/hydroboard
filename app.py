from flask import Flask, jsonify, make_response
from hydro_func import k_means

app = Flask(__name__)

@app.route("/kmeans/<humedad>/<precipitacion>", methods=["GET"])
def kmeans(humedad, precipitacion):
    return make_response(jsonify(prediccion=str(k_means(humedad, precipitacion))), 200)

if __name__ == "__main__":
    app.run(debug=True, port=5000)