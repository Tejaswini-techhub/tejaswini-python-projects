import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

DATA = 'salary_data.csv'
MODEL = 'salary_model.pkl'

def create_sample():
    # simple example data
    rows = [
        {'experience':1,'salary':30000},
        {'experience':2,'salary':40000},
        {'experience':3,'salary':50000},
        {'experience':4,'salary':60000},
        {'experience':5,'salary':70000},
    ]
    df = pd.DataFrame(rows)
    df.to_csv(DATA, index=False)

def train():
    if not os.path.exists(DATA):
        create_sample()
    df = pd.read_csv(DATA)
    X = df[['experience']]
    y = df['salary']
    model = LinearRegression()
    model.fit(X,y)
    joblib.dump(model, MODEL)
    print('Model trained and saved as', MODEL)

def predict(years):
    if not os.path.exists(MODEL):
        print('No model found. Training now...')
        train()
    model = joblib.load(MODEL)
    pred = model.predict([[years]])
    print(f'Predicted salary for {years} years experience: Rs {round(pred[0],2)}')

def main():
    while True:
        cmd = input('Type "train", "predict" or "exit": ').strip().lower()
        if cmd == 'train':
            train()
        elif cmd == 'predict':
            y = float(input('Enter years of experience: ').strip())
            predict(y)
        elif cmd == 'exit':
            break
        else:
            print('Unknown command.')

if __name__ == '__main__':
    main()
