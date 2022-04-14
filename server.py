from flask import Flask
app = Flask(__name__)

@app.route("/")
Add Debug Configuration
def hello():
    return "Hello Bala's World!"

if __name__ == "_main_":
    app.run(host=`0.0.0.0`)
        