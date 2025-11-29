from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from Flask on ML node!"

if __name__ == "__main__":
    print("About to start Flask app...")
    app.run(host="0.0.0.0", port=8080, debug=True)
    print("Flask app has started.")