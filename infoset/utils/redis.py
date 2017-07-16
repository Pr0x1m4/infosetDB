# Redis library
import redis
import pickle
import json

# Infoset-ng imports
from infoset.api import CONFIG


class Redis(object):
    def __init__(self):
        """Function for creating and initialising Redis.

        Args:

        Returns:
            Redis Instance configured with settings

        """
        host = CONFIG.redis_hostname()
        port = CONFIG.redis_port()
        self.redis = redis.StrictRedis(
            host=host, port=port, db=0, decode_responses=True)

    def set(self, key, data):
        """Function for setting keys to redis instance.

        Args:
            id_agent: Unique Identifier of an Infoset Agent

        Returns:
            Text response of Received

        """
        self.redis.set(str(key), json.dumps(data))

    def get(self, key):
        """Function for getting data from redis instance.

        Args:
            id_agent: Unique Identifier of an Infoset Agent

        Returns:
            Text response of Received

        """
        data = json.loads(self.redis.get(key))
        return data
