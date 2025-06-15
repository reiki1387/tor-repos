import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
from sklearn.cluster import KMeans

# Suppress any warning messages that might clutter the output
warnings.filterwarnings('ignore')

# Generate Synthetic Vehicle Data
np.random.seed(0)  # Set seed for reproducibility
data_size = 300    # Number of data points

# Create a dictionary with synthetic features: Weight, EngineSize, and Horsepower
data = {
    'Weight': np.random.randint(1000, 3000, data_size),         # Vehicle weight in kg (1000 to 3000)
    'EngineSize': np.random.uniform(1.0, 4.0, data_size),       # Engine size in liters (1.0L to 4.0L)
    'Horsepower': np.random.randint(50, 300, data_size)         # Engine power (50 to 300 HP)
}

# Convert the dictionary into a DataFrame for easy handling
df = pd.DataFrame(data)

# Prepare Data for Clustering
# No labels are needed for KMeans (unsupervised learning)
X = df  # Use the entire dataset for clustering

# Apply KMeans Clustering Algorithm
# Initialize KMeans with 3 clusters and a fixed random seed for consistent results
kmeans = KMeans(n_clusters=3, random_state=42)

# # Fit the model to the data (compute cluster centers and labels)
kmeans.fit(X)

# # Plot a 2D scatter plot using 'Weight' and 'Horsepower' as the axes
# # Color the points based on their cluster label assigned by KMeans
# plt.scatter(df['Weight'], df['Horsepower'], c=kmeans.labels_, cmap='viridis')

# # Add axis labels and a title for clarity
# plt.xlabel('Weight')
# plt.ylabel('Horsepower')
# plt.title('Vehicle Clusters')

# # Display the plot
# plt.show()


# Cluster Plot with Centroid
# Plot clusters based on 'Weight' and 'Horsepower'
# plt.figure(figsize=(8, 6))
# plt.scatter(df['Weight'], df['Horsepower'], c=kmeans.labels_, cmap='viridis', s=50)

# # Plot centroids
# centroids = kmeans.cluster_centers_
# plt.scatter(centroids[:, 0], centroids[:, 2], c='red', marker='x', s=200, label='Centroids')
# print(centroids)

# plt.xlabel('Weight')
# plt.ylabel('Horsepower')
# plt.title('Vehicle Clusters (Weight vs Horsepower)')
# plt.legend()
# plt.grid(True)
# plt.show()

# PCA 2D Projection
# from sklearn.decomposition import PCA

# # Reduce dimensions from 3 to 2
# pca = PCA(n_components=2)
# reduced_data = pca.fit_transform(df)

# # Plot PCA-reduced clusters
# plt.figure(figsize=(8, 6))
# plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=kmeans.labels_, cmap='viridis', s=50)

# plt.xlabel('Principal Component 1')
# plt.ylabel('Principal Component 2')
# plt.title('KMeans Clusters (PCA 2D Projection)')
# plt.grid(True)
# plt.show()


#3D Scatter Plot (Weight, EngineSize, Horsepower)
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot all three features with color-coded clusters
ax.scatter(df['Weight'], df['EngineSize'], df['Horsepower'],
           c=kmeans.labels_, cmap='viridis', s=50)

ax.set_xlabel('Weight')
ax.set_ylabel('Engine Size')
ax.set_zlabel('Horsepower')
ax.set_title('3D Vehicle Clusters')
plt.show()
