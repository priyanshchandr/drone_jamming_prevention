import pandas as pd
import numpy as np

# Function to generate synthetic dataset
def generate_data(num_samples=10000):
    np.random.seed(42)
    
    # Random signal strength (in dBm), ranging from -100 to 0 (typical values for Wi-Fi signals)
    signal_strength = np.random.uniform(-100, 0, num_samples)
    
    # Random distance (in meters) between 10m and 500m
    distance = np.random.uniform(10, 500, num_samples)
    
    # Random channel frequency: 2.4GHz or 5GHz (50% probability for each)
    channel_frequency = np.random.choice(['2.4GHz', '5GHz'], num_samples)
    
    # Jamming likelihood based on some synthetic rules
    # Assume jamming is more likely when signal strength is weak and distance is large
    jamming_likelihood = np.where((signal_strength < -50) & (distance > 200), 1, 0)
    
    # Create a DataFrame
    data = pd.DataFrame({
        'Signal_Strength': signal_strength,
        'Distance': distance,
        'Channel_Frequency': channel_frequency,
        'Jamming_Likelihood': jamming_likelihood
    })
    
    # Save to CSV
    data.to_csv('data/synthetic_channel_data.csv', index=False)
    print("Synthetic dataset saved to 'data/synthetic_channel_data.csv'")

# Generate data
generate_data()
