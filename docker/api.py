# Standard libraries
import sys
import os

# Try to create a working PYTHONPATH
_DOCKER_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
_ROOT_DIRECTORY = os.path.abspath(os.path.join(_DOCKER_DIRECTORY, os.pardir))
if _DOCKER_DIRECTORY.endswith('/infosetDB/docker') is True:
    sys.path.append(_ROOT_DIRECTORY)
else:
    print(
        'This script is not installed in the "infoset-ng/bin" directory. '
        'Please fix.')
    sys.exit(2)

from infoset.utils.configuration import Config
from infoset.api import API

config = Config()

API.run(host=config.listen_address(), port=config.bind_port())
