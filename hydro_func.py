import pandas as pd
from sklearn.cluster import KMeans

K = 5
UBICACION = "C:\\Users\\mauri\\OneDrive\\Escritorio\\UADE\\5° Año\\Proyecto Final de Ingeniería Informática\\hydroboard\\M_Datos-Colon.csv"

def k_means(humedad, precipitacion):
    data = pd.read_csv(UBICACION, sep=";", decimal=".")
    points = data[['Humedad', 'Precipitacion']].values
    sample = [[humedad, precipitacion]]
    kmeans = KMeans(n_clusters=K, random_state=0, n_init="auto")
    kmeans.fit(points)
    classification = kmeans.predict(sample)
    return classification[0]

