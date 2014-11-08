from flask import *

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def status():
  return "Hi!"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5555)
