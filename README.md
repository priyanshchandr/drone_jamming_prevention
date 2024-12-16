# Drone Jamming Prevention and Channel Allocation

This project aims to develop a system for detecting and preventing drone jamming by predicting jamming likelihood based on various features like signal strength, distance, and channel frequency. The system then allocates channels to drones using a double greedy algorithm to minimize interference, ensuring efficient communication and preventing jamming.

## Project Structure

```
/drone_jamming_prevention
├── /data
│   ├── synthethic_channel_data.csv          # Raw input data
│   ├── X_train.csv               # Training features
│   ├── X_test.csv                # Testing features
│   ├── y_train.csv               # Training labels
│   └── y_test.csv                # Testing labels
├── /results
│   ├── model.pkl                 # Trained machine learning model
│   └── allocation_results.txt    # Drone-to-channel allocation results
├── /src
│   ├── preprocess.py             # Data preprocessing script
│   ├── train_model.py            # Model training script
│   └── allocate_channels.py      # Channel allocation script using double greedy algorithm
├── README.md                     # Project overview and instructions
└── requirements.txt              # List of dependencies
```

## Features

- **Data Preprocessing**: Cleans and prepares the dataset by encoding categorical features and saving the processed data for model training.
- **Model Training**: Trains a RandomForestClassifier model to predict the likelihood of jamming based on signal strength, distance, and channel frequency.
- **Channel Allocation**: Allocates channels to drones using the double greedy algorithm, ensuring minimum interference.
- **Output**: Generates drone-to-channel allocation results in a text file (`allocation_results.txt`), including the mapping of drones to channels and their respective frequencies.

## Prerequisites

- Python 3.x
- Libraries: `pandas`, `scikit-learn`, `joblib`

To install the required dependencies, use the following command:

```bash
pip install -r requirements.txt
```

## Setup and Usage

Firstly replace synthetic_channel_data to your dataset.

### Step 1: Preprocess the Data
Run the `preprocess.py` script to preprocess the raw data.

```bash
python src/preprocess.py
```

This will clean and encode the data, saving the preprocessed data as CSV files.

### Step 2: Train the Model
Run the `train_model.py` script to train the machine learning model.

```bash
python src/train_model.py
```

This will train a RandomForestClassifier on the preprocessed training data and save the trained model as `model.pkl` in the `results` folder.

### Step 3: Allocate Channels
Run the `allocate_channels.py` script to predict jamming likelihood and allocate channels to drones.

```bash
python src/allocate_channels.py
```

This will load the trained model, make predictions on the test data, and use the double greedy algorithm to allocate channels. The results will be saved in `allocation_results.txt`.

### Example Output

The allocation results will be displayed and saved in the following format:

```
Drone 1 will use Channel 1 (2.4GHz)
Drone 2 will use Channel 3 (5GHz)
Drone 3 will use Channel 0 (2.4GHz)
Drone 4 will use Channel 2 (5GHz)
```

## Data Format

### Input Data (`channel_data.csv`)

The dataset consists of the following columns:

- `Signal_Strength`: The strength of the signal received by the drone (numeric value).
- `Distance`: The distance between the drone and the base station (numeric value).
- `Channel_Frequency`: The frequency of the channel (e.g., `2.4GHz` or `5GHz`).
- `Jamming_Likelihood`: The likelihood of jamming occurring for a given channel (numeric value between 0 and 1).

### Output Data (`allocation_results.txt`)

The file will contain the drone-to-channel allocation with the corresponding channel frequencies.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to adjust and customize this README file based on your project's specific requirements. Let me know if you need any more adjustments! 😊
