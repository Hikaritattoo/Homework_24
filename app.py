import os

from flask import Flask, request
from flask_restx import abort

import utils
from config import COMMANDS, DATA_DIR

app = Flask(__name__)


@app.route("/perform_query/", methods=["GET", "POST"])
def perform_query():
    cmd_1 = request.args.get('cmd_1') + '_'
    value1 = request.args.get('value1')
    cmd_2 = request.args.get('cmd_2') + '_'
    value2 = request.args.get('value2')
    file_name = request.args.get('file_name')

    if (
        None in (cmd_1,
                 value1,
                 cmd_2,
                 value2,
                 file_name)
        or cmd_1 not in COMMANDS
        or cmd_2 not in COMMANDS
    ):
        return abort(400, 'ParametersError')
    file_path = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_path):
        return abort(400, 'WrongFileName')
    try:
        with open(file_path, 'r') as f:
            result1 = getattr(utils, cmd_1)(f, value1)
            result2 = getattr(utils, cmd_2)(result1, value2)
    except (ValueError, TypeError) as e:
        abort(400, e)
    return app.response_class(result2, content_type="text/plain")


if __name__ == "__main__":
    app.run()


