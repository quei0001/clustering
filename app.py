import streamlit as st
import pandas as pd
from utils import load_data, preprocess_data
from predictor import run_kmeans
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Data Upload and Preprocessing
st.title("Clustering App")
st.write("Upload your CSV file for clustering analysis:")

uploaded_file = st.file_uploader("Choose a file", type=["csv"])

if uploaded_file is not None:
    # Load and preprocess data
    df = load_data(uploaded_file)
    
    st.write("Data Preview Before Preprocessing:")
    st.write(df.head())
    
    df = preprocess_data(df)
    
    st.write("Data Preview After Preprocessing:")
    st.write(df.head())
    
    # 2. KMeans Clustering
    st.write("Choose number of clusters:")
    k = st.slider("Number of Clusters", 2, 10, 3)
    
    st.write("Running KMeans...")
    clusters, centroids = run_kmeans(df, k)
    
    df['Cluster'] = clusters
    st.write("Clustered Data:")
    st.write(df.head())
    
    # 3. Visualization
    st.write("Visualizing Clusters")
    fig, ax = plt.subplots()
    sns.scatterplot(x='Feature1', y='Feature2', hue='Cluster', data=df, palette='Set2', ax=ax)
    st.pyplot(fig)
