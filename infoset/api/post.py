"""infoset-ng database API. Posting Routes."""

# Standard imports
import json
import celery
import pprint

# Flask imports
from flask import Blueprint, request, abort
from celery import Celery

# Infoset-ng imports
from infoset.utils import general
from infoset.api import CONFIG
from infoset.api import REDIS
from infoset.cache import cache
from infoset.utils import log


# Define the POST global variable
POST = Blueprint('POST', __name__)

# Define celery instance
celery = Celery("infoset", broker=CONFIG.redis_url(),
                backend=CONFIG.redis_url())


@celery.task
def process_cache(redis_key):
    data = REDIS.get(redis_key)
    processed = cache.ProcessRedisCache(data)


@POST.route('/receive/<id_agent>', methods=['POST'])
def receive(id_agent):
    """Function for handling /infoset/api/v1.0/receive/<id_agent> route.

    Args:
        id_agent: Unique Identifier of an Infoset Agent

    Returns:
        Text response of Received

    """
    # Initialize key variables
    found_count = 0

    # Read configuration
    cache_dir = CONFIG.ingest_cache_directory()

    # Get JSON from incoming agent POST
    data = request.json
    # Make sure all the important keys are available
    keys = ['timestamp', 'id_agent', 'devicename']
    for key in keys:
        if key in data:
            found_count += 1

    # Do processing
    if found_count == 3:
        # Extract key values from posting
        try:
            timestamp = int(data['timestamp'])
        except:
            abort(404)
        id_agent = data['id_agent']
        devicename = data['devicename']

        # Create a hash of the devicename
        device_hash = general.hashstring(devicename, sha=1)

        redis_key = (
            '%s-%s-%s') % (timestamp, id_agent, device_hash)
        REDIS.set(redis_key, data)

        result = process_cache.delay(redis_key)

        # Return
        return 'OK'

    else:
        abort(404)
