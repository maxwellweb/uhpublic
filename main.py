from flask import Flask

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def hello_worl():
    return "<p>Hola Mundo</p>"

# run the application
if __name__ == "__main__":
    app.run(debug=True)