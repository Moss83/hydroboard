import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.spatial import Voronoi, voronoi_plot_2d

k = int(input("Ingrese cantidad de clusters: "))

humedad = float(input("Ingrese la humedad mensual (%): "))
precipitacion = float(input("Ingrese la precipitación mensual (mm): "))

ubicacion="C:\\Users\\mauri\\OneDrive\\Escritorio\\UADE\\5° Año\\Proyecto Final de Ingeniería Informática\\hydroboard\\M_Datos-Colon.csv"
data = pd.read_csv(ubicacion, sep=";", decimal=".")

points = data[['Humedad', 'Precipitacion']].values

sample = [[humedad, precipitacion]]

kmeans = KMeans(n_clusters=k, random_state=0, n_init="auto")
kmeans.fit(points)
classification = kmeans.predict(sample)

cluster_labels = kmeans.labels_
cluster_centers = kmeans.cluster_centers_

vor = Voronoi(cluster_centers)

fig, ax = plt.subplots(figsize=(8, 6))
voronoi_plot_2d(vor, ax=ax)
ax.scatter(points[:, 0], points[:, 1], cmap="rainbow", c=cluster_labels, s=50)
ax.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='black', marker='x', s=100, label='Centroides')
ax.scatter(sample[0][0], sample[0][1], c=classification, marker='o', s=200)
plt.xlim(data['Humedad'].min() - 1, data['Humedad'].max() + 1)
plt.ylim(data['Precipitacion'].min() - 1, data['Precipitacion'].max() + 1)
plt.xlabel('Humedad')
plt.ylabel('Precipitacion')
plt.title('Diagrama de Voronoi: Resultado del modelo')
plt.legend()
plt.show()
