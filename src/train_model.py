from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from joblib import dump
import pandas as pd

def train_model():
    # Load preprocessed data
    X_train = pd.read_csv('data/X_train.csv')
    X_test = pd.read_csv('data/X_test.csv')
    y_train = pd.read_csv('data/y_train.csv').squeeze()  # Ensure y is 1D
    y_test = pd.read_csv('data/y_test.csv').squeeze()    # Ensure y is 1D

    # Train Random Forest Model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))

    # Save the model
    dump(model, 'results/model.pkl')
    print("Model saved to results/model.pkl")

if __name__ == "__main__":
    train_model()

