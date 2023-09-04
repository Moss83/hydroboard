import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.spatial import Voronoi, voronoi_plot_2d

ubicacion="C:\\Users\\mauri\\OneDrive\\Escritorio\\UADE\\5° Año\\Proyecto Final de Ingeniería Informática\\hydroboard\\M_Datos-Colon.csv"
data = pd.read_csv(ubicacion, sep=";", decimal=".")

points = data[['Humedad', 'Precipitacion']].values

K = 6
sample = [[84, 57]]

kmeans = KMeans(n_clusters=K, random_state=0, n_init="auto")
kmeans.fit(points)
clasification = kmeans.predict(sample)

print(clasification)


cluster_labels = kmeans.labels_
cluster_centers = kmeans.cluster_centers_

print(cluster_labels)

vor = Voronoi(cluster_centers)

fig, ax = plt.subplots(figsize=(8, 6))
voronoi_plot_2d(vor, ax=ax)
ax.scatter(points[:, 0], points[:, 1], cmap="rainbow", c=cluster_labels, s=50)
ax.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='black', marker='x', s=100, label='Centroides')
ax.scatter(sample[0][0], sample[0][1], cmap=clasification, marker='o', s=200)
plt.xlim(data['Humedad'].min() - 1, data['Humedad'].max() + 1)
plt.ylim(data['Precipitacion'].min() - 1, data['Precipitacion'].max() + 1)
plt.xlabel('Humedad')
plt.ylabel('Precipitacion')
plt.title('Diagrama de Voronoi: Resultado del modelo')
plt.legend()
plt.show()
