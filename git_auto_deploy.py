from flask import Flask
from flask import request
from werkzeug.exceptions import BadRequest
import json
import os
import subprocess

app = Flask(__name__)


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@app.route("/", methods=['POST'])
def auto_deploy():
    # try:
    repository_url = request.get_json()['repository']['clone_url']
    repo_info = get_repositories_list(repository_url)
    subprocess.Popen(repo_info['local_location'] + '/' + repo_info['script'],cwd=repo_info['local_location'], shell=True, executable="/bin/bash")
    # except TypeError:
    #     return BadRequest()
    return repository_url

def get_repositories_list(respository_url):
    with open(os.path.dirname(os.path.realpath(__file__)) + '/repositories.json') as data_file:
        data = json.load(data_file)['repositories']
    for repo in data:
        if repo['url'] == respository_url:
            return repo
    raise NotImplemented




if __name__ == '__main__':
    app.run(host= '0.0.0.0')
