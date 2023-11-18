import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Bidirectional, Dropout, SpatialDropout1D
from tensorflow.keras.optimizers import Adam
from sklearn.utils.class_weight import compute_sample_weight
import numpy as np
import joblib

#берем данные и объединяем их
data1 = pd.read_csv('./data/eminem.csv')
data2 = pd.read_csv('./data/lfmao.csv')
combined_data = pd.concat([data1, data2], ignore_index=True)

#делаем 2 набора данных (тест и тренировка)
train_data, test_data = train_test_split(combined_data, test_size=0.2, random_state=42)

#подготовка \ берем данные из CONTENT
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(train_data['CONTENT']).toarray()
X_test = vectorizer.transform(test_data['CONTENT']).toarray()

#подготовка \ берем данные из CLASS 
#для последующего определения верен ли результат или нет
label_encoder = LabelEncoder()
y_train = label_encoder.fit_transform(train_data['CLASS'])
y_test = label_encoder.transform(test_data['CLASS'])

#сохранение CountVectorizer (преобразует данные в матрицы для обработки)
joblib.dump(vectorizer, 'vectorizer.pkl')

#веса для балансировки
class_weights = compute_sample_weight(class_weight='balanced', y=y_train)

#модель
model = Sequential([
    Embedding(input_dim=len(vectorizer.get_feature_names_out()), 
    output_dim=32, 
    input_length=X_train.shape[1]),
    SpatialDropout1D(0.2),
    Bidirectional(LSTM(100)),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])

#внедряем веса
model.compile(loss='binary_crossentropy', optimizer=Adam(), metrics=['accuracy'])

#обучение
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2, sample_weight=class_weights)

#сохранение самой модели
model.save('your_model.h5')

#сохранение LabelEncoder \ обратная работа vectorizer
joblib.dump(label_encoder, 'label_encoder.pkl')
