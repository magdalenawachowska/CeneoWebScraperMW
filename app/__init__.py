from flask import Flask

app = Flask(__name__)                #tworzenie aplikacji

from app import routes 

if __name__ == '__main__':
    app.run(debug=True)