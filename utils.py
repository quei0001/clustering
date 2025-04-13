import pandas as pd

# Function to load the data from the CSV file
def load_data(uploaded_file):
    df = pd.read_csv(uploaded_file)
    return df

# Function to preprocess the data
def preprocess_data(df):
    # Debugging: Check the data types before preprocessing
    print("Data types before preprocessing:", df.dtypes)
    
    # Convert all columns to numeric, force non-numeric entries to NaN
    df = df.apply(pd.to_numeric, errors='coerce')
    
    # Debugging: Check the data types after preprocessing
    print("Data types after preprocessing:", df.dtypes)
    
    # Handle NaN or infinite values
    df = df.fillna(0)  # Replace NaN values with 0 or apply other methods if necessary
    
    print("Data preview after preprocessing:")
    print(df.head())
    
    return df
