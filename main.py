import os

# Run preprocessing
os.system('python src/preprocess.py')

# Train model
os.system('python src/train_model.py')

# Allocate channels
os.system('python src/allocate_channels.py')
