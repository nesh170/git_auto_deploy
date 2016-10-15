from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/", methods=['POST'])
def auto_deploy():
    return str(request.get_json()['repository']['clone_url'])


if __name__ == '__main__':
    app.run(host= '0.0.0.0')
