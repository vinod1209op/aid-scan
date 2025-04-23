from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense


def build_autoencoder(seq_length, num_features):
    model = Sequential([
        LSTM(128, input_shape=(seq_length, num_features), return_sequences=True),
        LSTM(64, return_sequences=False),
        Dense(128, activation='relu'),
        Dense(num_features)
    ])
    model.compile(optimizer='adam', loss='mse')
    return model
