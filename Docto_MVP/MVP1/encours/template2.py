from flask import Flask
app = Flask(__name__)

@app.route('///C://Users//thoma//Desktop//1erMVP//candidate.html')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
    print(hello_world())
