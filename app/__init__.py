from flask import Flask

app = Flask(__name__)                #tworzenie aplikacji

from app import routes 

app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)