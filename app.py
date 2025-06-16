from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def home():
    return "Hello from Flask on Azure App Service with Python 3.11!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
