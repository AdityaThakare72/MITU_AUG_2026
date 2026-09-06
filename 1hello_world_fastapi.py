from fastapi import FastAPI

app = FastAPI()


@app.get('/')    # '/' => route
def hello():
    return f"hello, Welcome to fastapi"


@app.get('/info')
def info():
    return {'name': 'Aditya Thakare',
            'des': 'Data Scientist'}