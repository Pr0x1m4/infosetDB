"""infoset-ng configuration ui."""

# Flask imports
from flask import Blueprint
from flask import render_template
from flask import request
from infoset.utils import configuration
import os
import yaml

# Define the STATUS global variable
CONFIG_PAGE = Blueprint('CONFIG_PAGE', __name__)


@CONFIG_PAGE.route('/config/get')
def get_config_page():
    """Function for displaying the current configuration status.

    Args:
        None

    Returns:
        Configuration Page

    """
    # Return
    configDict = _get_config()
    return render_template('config.html', config=configDict)

@CONFIG_PAGE.route('/config/update',methods=['POST'])
def update_config():
    """Function for displaying the current configuration status.

    Args:
        None

    Returns:
        Configuration Page

    """
    config_field_dict = _get_config_field_dict()

    new_yaml_obj = {'main':{}}
    
    for field_name, setting_name in config_field_dict.items():
        value = request.form.get(field_name)
        try:
            #If a value can be converted to an int, do so...
            value = int(value)
        except:
            pass
        new_yaml_obj['main'][setting_name] = value

    
    dirname, filename = os.path.split(os.path.abspath(__file__))
    config_file_path = dirname + '/../../etc/config.yaml'
    config_file = open(config_file_path, 'w')

    yaml_text = yaml.dump(new_yaml_obj, config_file,default_flow_style=False)

    return get_config_page()

def _get_config():
    """Function for retrieving the current configuration and placing it into a dict. The dict's keys match the form field names in config.html
    Args:
        None

    Returns:
        Configuration Dictionary

    """    
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

def _get_config_field_dict():
    """Maps the config form field names to the names of the settings in the YAML file

    Args:
        None

    Returns:
        Configuration form field map

    """    
    config_field_dict = {
        'infoset-username':'username',
        'infoset-port':'bind_post',
        'db-name':'db_name',
        'db-host':'db_hostname',
        'db-username':'db_username',
        'db-password':'db_password',
        'ingester-cache':'ingest_cache_directory',
        'ingester-interval':'interval',
        'ingester-pool-size':'ingest_pool_size',
        'ingester-listen-address':'listen_address',
        'log-directory':'log_directory',
        'log-level':'log_level',
        'memcached-host':'memcached_hostname',
        'memcached-port':'memcached_port',
        'sqlalchemy-overflow':'sqlalchemy_max_overflow',
        'sqlalchemy-pool-size':'sqlalchemy_pool_size',
        'infoset-username':'username',
        'infoset-port':'bind_port'
    }
    return config_field_dict


