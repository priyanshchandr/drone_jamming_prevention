import pandas as pd
from sklearn.model_selection import train_test_split

def preprocess_data(filepath):
    data = pd.read_csv(filepath)
    
    # Normalize signal strength and distance
    data['Signal_Strength'] = (data['Signal_Strength'] - data['Signal_Strength'].mean()) / data['Signal_Strength'].std()
    data['Distance'] = (data['Distance'] - data['Distance'].mean()) / data['Distance'].std()
    
    # Encode Channel Frequency
    data['Channel_Frequency'] = data['Channel_Frequency'].apply(lambda x: 0 if x == '2.4GHz' else 1)
    
    # Split features and target
    X = data[['Signal_Strength', 'Distance', 'Channel_Frequency']]
    y = data['Jamming_Likelihood']
    
    return train_test_split(X, y, test_size=0.2, random_state=42)

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = preprocess_data('data/synthetic_channel_data.csv')
    print("Data preprocessed successfully!")

    X_train.to_csv('data/X_train.csv', index=False)
    X_test.to_csv('data/X_test.csv', index=False)
    y_train.to_csv('data/y_train.csv', index=False)
    y_test.to_csv('data/y_test.csv', index=False)
    print("Preprocessed data saved successfully!")

