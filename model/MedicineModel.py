import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB



def preprocess_text(text):
    if isinstance(text, float):
        return ''
    text = text.strip('"""""""')
    
    words = nltk.word_tokenize(text)
      
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    
    processed_text = ' '.join(words)
    
    return processed_text


def train_Medicine_Model(data):
    data['Description'] = data['Description'].apply(preprocess_text)
    
    X_train = data['Description']
    y_train = data['Drug_Name']
    
    
    vectorizer = CountVectorizer()
    X_train_vectors = vectorizer.fit_transform(X_train)
    
    model = MultinomialNB()
    model.fit(X_train_vectors, y_train)
    
    with open('./model/medicineModel.pkl', 'wb') as f:
        pickle.dump((model, vectorizer), f)


def predict_using_model(new_data):
    with open('./model/medicineModel.pkl', 'rb') as f:
        model, vectorizer = pickle.load(f)
    new_data['Description'] = new_data['Description'].apply(preprocess_text)
    
    new_data_vectors = vectorizer.transform(new_data['Description'])
    
    predictions = model.predict(new_data_vectors)
    
    return predictions

def main():
    data = pd.read_csv('./data/Medicine_description.csv')
    
    print('Enter 1 to train the model or 2 to use an existing model for prediction:')
    choice = int(input())
    
    if choice == 1:
        train_Medicine_Model(data)
        print('Model training complete. Model saved as model.pkl.')
    elif choice == 2:
        print('Enter symptoms in natural language:')
        symptoms = input()
        
        new_data = pd.DataFrame({'Description': [symptoms]})
        
        drug_name = predict_using_model(new_data)
        print('Predicted drug name:', drug_name[0])
    else:
        print('Invalid choice.')


if __name__ == '__main__':
    main()
