import joblib
from tensorflow.keras.models import load_model

def do_prediction(message):

    #подгрузка модели
    loaded_model = load_model('./Model/your_model.h5')
    loaded_label_encoder = joblib.load('./Model/label_encoder.pkl')
    loaded_vectorizer = joblib.load('./Model/vectorizer.pkl')

    #получение сообщения
    input_text = [message]
    X_input = loaded_vectorizer.transform(input_text).toarray()


    y_pred_prob = loaded_model.predict(X_input)
    #print(y_pred_prob) #вывод шанса \ отладка

    #преобразование шанса в 1, если он >0.515
    threshold = 0.515
    y_pred = (y_pred_prob > threshold).astype(int)
    predicted_class = loaded_label_encoder.inverse_transform(y_pred)

    #вывод результата
    print(f'Предсказанный класс: {predicted_class[0]}') #отладка
    return y_pred
