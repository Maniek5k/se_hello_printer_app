from flask import Flask
app = Flask(__name__)

import hello_world.views    # noqa: W292, F401, E402
