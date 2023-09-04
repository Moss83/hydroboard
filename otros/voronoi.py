import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.spatial import Voronoi, voronoi_plot_2d

# Generar datos de ejemplo
np.random.seed(0)
x = np.random.rand(60, 2) * 20

print(x[:, 0])

# Número de clusters para K-means
num_clusters = 3

# Aplicar K-means
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
kmeans.fit(x)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Crear el diagrama de Voronoi
vor = Voronoi(centroids)

# Graficar los datos y el diagrama de Voronoi
fig, ax = plt.subplots(figsize=(8, 6))
voronoi_plot_2d(vor, ax=ax)
ax.scatter(x[:, 0], x[:, 1], c=labels, cmap='rainbow', s=50)
ax.scatter(centroids[:, 0], centroids[:, 1], c='black', marker='x', s=100, label='Centroids')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Diagrama de Voronoi con K-means')
plt.legend()
plt.show()
