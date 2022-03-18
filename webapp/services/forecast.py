import tensorflow as tf
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler
from sklearn.externals import joblib
from Models.database import engine


# # Recreate the exact same model, including its weights and the optimizer
# # new_model = tf.keras.models.load_model('services/multi_step_lstm.h5')

# # Show the model architecture
# # print(new_model.summary())


