from sklearn.cluster import KMeans

# Function to run KMeans clustering
def run_kmeans(df, k):
    # Assume 'Feature1' and 'Feature2' are the features you want to cluster
    features = df[['Feature1', 'Feature2']]  # Adjust according to your dataset

    # Run KMeans clustering
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(features)
    
    # Return the clusters and centroids
    return kmeans.labels_, kmeans.cluster_centers_
