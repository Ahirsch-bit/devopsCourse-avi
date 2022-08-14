from flask import Flask

app = Flask(__name__)


@app.route('/content')
def content():
    f = open("content.txt", "r", encoding="utf-8")
    content = f.read()
    f.close()
    return content, 200


@app.route('/register')
def register():
    file = open("newfile.txt", "a")
    file.write("Welcome!" + "\n")
    file.close()
    return "Success", 201


app.run(host='localhost', port=4000)
