"""Initialize the API module."""

# Import PIP3 libraries
from flask import Flask

#############################################################################
# Import configuration.
# This has to be done before all other infoset imports.
#############################################################################
from infoset.utils import configuration
CONFIG = configuration.Config()
#############################################################################
#############################################################################

from infoset.utils import redis
REDIS = redis.Redis()

# Configure the cache

# Define the global URL prefix
from infoset.constants import API_PREFIX

# Import API Blueprints
from infoset.api.post import POST
from infoset.api.status import STATUS
#from infoset.api.config_page import CONFIG_PAGE

from infoset.api.resources.agents import AGENTS
from infoset.api.resources.datapoints import DATAPOINTS
from infoset.api.resources.lastcontacts import LASTCONTACTS
from infoset.api.resources.devices import DEVICES
from infoset.api.resources.deviceagents import DEVICEAGENTS

from flask_graphql import GraphQLView

from infoset.db.db_orm import SESSION
from infoset.api.schema import schema, Datapoint

# Setup API and intialize the cache
API = Flask(__name__)

#API.debug = True
API.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # for having the GraphiQL interface
    )
)


@API.teardown_appcontext
def shutdown_session(exception=None):
    SESSION.remove()


# Register Blueprints
API.register_blueprint(POST, url_prefix=API_PREFIX)
API.register_blueprint(STATUS, url_prefix=API_PREFIX)
API.register_blueprint(DATAPOINTS, url_prefix=API_PREFIX)
API.register_blueprint(AGENTS, url_prefix=API_PREFIX)
API.register_blueprint(LASTCONTACTS, url_prefix=API_PREFIX)
API.register_blueprint(DEVICES, url_prefix=API_PREFIX)
API.register_blueprint(DEVICEAGENTS, url_prefix=API_PREFIX)
#API.register_blueprint(CONFIG_PAGE, url_prefix=API_PREFIX)
