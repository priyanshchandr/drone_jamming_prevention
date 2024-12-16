from joblib import load
import pandas as pd
from double_greedy import double_greedy
from sklearn.preprocessing import LabelEncoder

# Channel Frequency Map
CHANNEL_FREQUENCY_MAP = {
    0: '2.4GHz',
    1: '5GHz',
    2: '2.4GHz',
    3: '5GHz',
    4: '2.4GHz',
}

def allocate_channels():
    # Load the dataset
    data = pd.read_csv('data/synthetic_channel_data.csv')


    # Encode 'Channel_Frequency' to numeric values (0 and 1)
    label_encoder = LabelEncoder()
    data['Channel_Frequency'] = label_encoder.fit_transform(data['Channel_Frequency'])

    # Load the trained model
    model = load('results/model.pkl')

    # Predict jamming likelihood
    X = data[['Signal_Strength', 'Distance', 'Channel_Frequency']]
    predicted_jamming = model.predict_proba(X)[:, 1]

    # Instead of Drone_ID, you can simply use indices for allocation
    drones = range(len(data))  # This will create an index for each row, assuming each row represents a drone
    channels = range(len(predicted_jamming))  # Index-based channels

    # Run the double greedy algorithm
    allocation = double_greedy(drones, channels, {i: p for i, p in enumerate(predicted_jamming)})
    
    # # Prepare output string to print and save
    # output = "Drone-to-channel allocation:\n"
    # for drone, channel in allocation.items():
    #         # Ensure the channel is within the valid range of your map
    #         valid_channel = channel % len(CHANNEL_FREQUENCY_MAP)  # Wrap around if the channel is out of range
    #         if valid_channel in CHANNEL_FREQUENCY_MAP:
    #             f.write(f"Drone {drone+1} will use Channel {valid_channel} ({CHANNEL_FREQUENCY_MAP[valid_channel]})\n")
    #         else:
    #             f.write(f"Drone {drone+1} will use Channel {valid_channel} (Unknown Frequency)\n")

    # # Print the allocation
    # print(output)

    # # Save results to the file
    # with open('results/allocation_results.txt', 'w') as f:
    #     f.write(output)
    # Open the results file and write the allocation
    with open('results/allocation_results.txt', 'w') as f:  # Open file in write mode
        for drone, channel in allocation.items():
            # Ensure the channel is within the valid range of your map
            valid_channel = channel % len(CHANNEL_FREQUENCY_MAP)  # Wrap around if the channel is out of range
            if valid_channel in CHANNEL_FREQUENCY_MAP:
                f.write(f"Drone {drone+1} will use Channel {valid_channel} ({CHANNEL_FREQUENCY_MAP[valid_channel]})\n")
            else:
                f.write(f"Drone {drone+1} will use Channel {valid_channel} (Unknown Frequency)\n")

if __name__ == "__main__":
    allocate_channels()
