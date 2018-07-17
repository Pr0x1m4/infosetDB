#!/usr/bin/env python3
"""infoset classes that manage various configurations."""

import os.path
import os

# Import project libraries
from infoset.utils import general
from infoset.utils import log
import infoset.env as env


class Config(object):
    """Class gathers all configuration information."""

    def __init__(self):
        """Function for intializing the class.

        Args:
            None

        Returns:
            None

        """

    def db_file(self):
        """Determine the SQLite database file.

        Args:
            None

        Returns:
            value: configured SQLite db_file

        """
        # Return
        return env.DB_FILE

    def ingest_cache_directory(self):
        """Determine the ingest_cache_directory.

        Args:
            None

        Returns:
            value: configured ingest_cache_directory

        """
        # Get cache directory
        value = env.CACHE_DIRECTORY

        # Check if value exists
        if os.path.isdir(value) is False:
            log_message = (
                'CACHE_DIRECTORY: "%s" '
                'does not exist.') % (value)
            log.log2die(1011, log_message)

        # Return
        return value

    def ingest_failures_directory(self):
        """Determine the ingest_failures_directory.

        Args:
            None

        Returns:
            value: configured ingest_failures_directory

        """
        # Get parameter
        value = ('%s/failures') % (self.ingest_cache_directory())

        # Check if value exists
        if os.path.exists(value) is False:
            os.makedirs(value, mode=0o755)

        # Return
        return value

    def db_name(self):
        """Get db_name.

        Args:
            None

        Returns:
            result: result

        """

        # Process configuration
        result = env.DB_NAME

        # Get result
        return result

    def db_username(self):
        """Get db_username.

        Args:
            None

        Returns:
            result: result

        """
        # Get result
        return env.DB_USERNAME

    def db_password(self):
        """Get db_password.

        Args:
            None

        Returns:
            result: result

        """

        # Get result
        return env.DB_PASSWORD

    def db_hostname(self):
        """Get db_hostname.

        Args:
            None

        Returns:
            result: result

        """
        # Get result
        return env.DB_HOSTNAME

    def listen_address(self):
        """Get listen_address.

        Args:
            None

        Returns:
            result: result

        """

        result = env.ADDRESS

        # Default to 0.0.0.0
        if result is None:
            result = '0.0.0.0'
        return result

    def interval(self):
        """Get interval.

        Args:
            None

        Returns:
            result: result

        """
        intermediate = env.INTERVAL

        # Default to 300
        if intermediate is None:
            result = 300
        else:
            result = int(intermediate)
        return result

    def bind_port(self):
        """Get bind_port.

        Args:
            None

        Returns:
            result: result

        """

        intermediate = env.PORT

        # Default to 8000
        if intermediate is None:
            result = 8000
        else:
            result = 8000  # int(intermediate)
        return result

    def ingest_pool_size(self):
        """Get ingest_pool_size.

        Args:
            None

        Returns:
            result: result

        """
        intermediate = env.INGEST_POOL_SIZE

        # Default to 20
        if intermediate is None:
            result = 20
        else:
            result = int(intermediate)
        return result

    def sqlalchemy_pool_size(self):
        """Get sqlalchemy_pool_size.

        Args:
            None

        Returns:
            result: result

        """
        intermediate = env.SQLALCHEMY_POOL_SIZE

        # Set default
        if intermediate is None:
            result = 10
        else:
            result = int(intermediate)
        return result

    def redis_hostname(self):
        """Get redis_hostname.

        Args:
            None

        Returns:
            result: result

        """
        result = env.REDIS_HOSTNAME

        # Default to localhost
        if result is None:
            result = 'localhost'
        return result

    def redis_port(self):
        """Get redis_port.

        Args:
            None

        Returns:
            result: result

        """
        intermediate = env.REDIS_PORT

        # Set default
        if intermediate is None:
            result = 6379
        else:
            result = int(intermediate)
        return result

    def redis_url(self):
        """Get redis url.

        Args:
            None

        Returns:
            result: result

        """

        return ("redis://%s:%s/0") % (self.redis_hostname(), self.redis_port())

    def sqlalchemy_max_overflow(self):
        """Get sqlalchemy_max_overflow.

        Args:
            None

        Returns:
            result: result

        """
        intermediate = env.SQLALCHEMY_MAX_OVERFLOW

        # Set default
        if intermediate is None:
            result = 10
        else:
            result = int(intermediate)
        return result

    def log_directory(self):
        """Determine the log_directory.

        Args:
            None

        Returns:
            value: configured log_directory

        """
        # Process configuration
        value = env.LOG_DIRECTORY

        # Check if value exists
        if os.path.isdir(value) is False:
            log_message = (
                'log_directory: "%s" '
                'in configuration doesn\'t exist!') % (value)
            log.log2die(1030, log_message)

        # Return
        return value

    def log_file(self):
        """Get log_file.

        Args:
            None

        Returns:
            result: result

        """
        # Get new result
        # print()
        #result = ('%s/infoset-ng.log') % (self.log_directory())
        result = "./log/infoset-ng.log"
        # Return
        return result

    def web_log_file(self):
        """Get web_log_file.

        Args:
            None

        Returns:
            result: result

        """
        # Get new result
        result = ('%s/api-web.log') % (self.log_directory())

        # Return
        return result

    def log_level(self):
        """Get log_level.

        Args:
            None

        Returns:
            result: result

        """
        # Get result
        sub_key = 'log_level'
        result = None
        key = 'main'

        # Get new result
        result = env.LOG_LEVEL

        # Return
        return result
