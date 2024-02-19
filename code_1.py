from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Witaj, świecie! To jest moja strona'

if __name__ == '__main__':
    app.run(debug=True)