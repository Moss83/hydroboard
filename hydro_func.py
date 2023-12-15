import pandas as pd
from sklearn.cluster import KMeans

K = 10
UBICACION = "C:\\Users\\mauri\\OneDrive\\Escritorio\\UADE\\5° Año\\Proyecto Final de Ingeniería Informática\\hydroboard\\Data\\M_El Palmar.csv"

def k_means(temp, humedad, viento, prec, ffmc, dmc, dc):
    data = pd.read_csv(UBICACION, sep=";", decimal=".")
    points = data[['TEMP', 'H.R.', 'VIENTO', 'PREC', 'FFMC', 'DMC', 'DC']].values
    sample = [[temp, humedad, viento, prec, ffmc, dmc, dc]]
    kmeans = KMeans(n_clusters=K, random_state=0, n_init="auto")
    kmeans.fit(points)
    classification = kmeans.predict(sample)
    return classification[0]

