"""infoset-ng configuration ui."""

# Flask imports
from flask import Blueprint
from flask import render_template
from infoset.utils import configuration
import os

# Define the STATUS global variable
CONFIG_PAGE = Blueprint('CONFIG_PAGE', __name__)


@CONFIG_PAGE.route('/config/get')
def getConfig():
    """Function for displaying the current configuration status.

    Args:
        None

    Returns:
        Configuration Page

    """
    # Return
    configDict = getCurrentConfigFileContents()
    return render_template('config.html', config=configDict)

def getCurrentConfigFileContents():
    configDict = {}
    config = configuration.Config()
    configDict['infoset-username'] = config.username()
    configDict['infoset-port'] = config.bind_port()

    configDict['db-name'] = config.db_name()
    configDict['db-host'] = config.db_hostname()
    configDict['db-username'] = config.db_username()
    configDict['db-password'] = config.db_password()

    configDict['ingester-cache'] = config.ingest_cache_directory()
    configDict['ingester-interval'] = config.interval()
    configDict['ingester-pool-size'] = config.ingest_pool_size()
    configDict['ingester-listen-address'] = config.listen_address()

    configDict['log-directory'] = config.log_directory()
    configDict['log-level'] = config.log_level()

    configDict['memcached-host'] = config.memcached_hostname()
    configDict['memcached-port'] = config.memcached_port()

    configDict['sqlalchemy-overflow'] = config.sqlalchemy_max_overflow()
    configDict['sqlalchemy-pool-size'] = config.sqlalchemy_pool_size()
    return configDict

