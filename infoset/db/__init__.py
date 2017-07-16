#!/usr/bin/env python3
"""Infoset ORM classes.

Manages connection pooling among other things.

"""

# Main python libraries
import os
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy import event
from sqlalchemy import exc

# Infoset libraries
from infoset.utils import configuration
from infoset.utils import log
from infoset.db import db_orm

#############################################################################
# Setup a global pool for database connections
#############################################################################
POOL = None
URL = None
TEST_ENGINE = None


def main():
    """Process agent data.

    Args:
        None

    Returns:
        None

    """
    # Initialize key variables
    use_mysql = True
    global POOL
    global URL
    global TEST_ENGINE

    # Get configuration
    config = configuration.Config()

    # Define SQLAlchemy parameters from configuration
    pool_size = config.sqlalchemy_pool_size()
    max_overflow = config.sqlalchemy_max_overflow()

    # Create DB connection pool
    if use_mysql is True:
        create_sqlite_if_not_exist(config)
        URL = ('sqlite:///%s') % (
            config.db_file())

        # Add MySQL to the pool
        db_engine = create_engine(
            URL, echo=False)

        # Fix for multiprocessing
        _add_engine_pidguard(db_engine)

        POOL = sessionmaker(
            autoflush=True,
            autocommit=False,
            bind=db_engine
        )

    else:
        POOL = None

    # Populate the test engine if this is a test database
    if config.db_name().startswith('test_') is True:
        TEST_ENGINE = db_engine


def create_sqlite_if_not_exist(config):
    if not os.path.isfile(config.db_file()):
        try:
            connection = sqlite3.connect(config.db_file())
            connection.execute("""CREATE TABLE iset_department (
                idx_department BIGINT NOT NULL, 
                code BLOB, 
                name BLOB, 
                enabled INTEGER DEFAULT '1', 
                ts_modified DATETIME DEFAULT CURRENT_TIMESTAMP, 
                ts_created DATETIME DEFAULT CURRENT_TIMESTAMP, 
                PRIMARY KEY (idx_department), 
                UNIQUE (code)
            );""")

            connection.execute("""CREATE TABLE iset_device (
                idx_device BIGINT NOT NULL, 
                devicename BLOB, 
                description BLOB, 
                enabled INTEGER DEFAULT '1', 
                ts_modified DATETIME DEFAULT CURRENT_TIMESTAMP, 
                ts_created DATETIME DEFAULT CURRENT_TIMESTAMP, 
                PRIMARY KEY (idx_device), 
                UNIQUE (devicename)
            );""")

            connection.execute("""CREATE TABLE iset_billcode (
                idx_billcode BIGINT NOT NULL, 
                code BLOB, 
                name BLOB, 
                enabled INTEGER DEFAULT '1', 
                ts_modified DATETIME DEFAULT CURRENT_TIMESTAMP, 
                ts_created DATETIME DEFAULT CURRENT_TIMESTAMP, 
                PRIMARY KEY (idx_billcode), 
                UNIQUE (code)
            );""")

            connection.execute("""CREATE TABLE iset_agentname (
                idx_agentname BIGINT NOT NULL, 
                name BLOB, 
                enabled INTEGER DEFAULT '1', 
                ts_modified DATETIME DEFAULT CURRENT_TIMESTAMP, 
                ts_created DATETIME DEFAULT CURRENT_TIMESTAMP, 
                PRIMARY KEY (idx_agentname), 
                UNIQUE (name)
            );""")

            connection.execute("""CREATE TABLE iset_agent (
                idx_agent BIGINT NOT NULL, 
                idx_agentname BIGINT DEFAULT '1' NOT NULL, 
                id_agent VARCHAR(100), 
                enabled INTEGER DEFAULT '1', 
                ts_modified DATETIME DEFAULT CURRENT_TIMESTAMP, 
                ts_created DATETIME DEFAULT CURRENT_TIMESTAMP, 
                PRIMARY KEY (idx_agent), 
                FOREIGN KEY(idx_agentname) REFERENCES iset_agentname (idx_agentname), 
                UNIQUE (id_agent)
            );""")

            connection.execute("""CREATE TABLE iset_deviceagent (
                idx_deviceagent BIGINT NOT NULL, 
                idx_device BIGINT DEFAULT '1' NOT NULL, 
                idx_agent BIGINT DEFAULT '1' NOT NULL, 
                enabled INTEGER DEFAULT '1', 
                last_timestamp BIGINT DEFAULT '0' NOT NULL, 
                ts_modified DATETIME DEFAULT CURRENT_TIMESTAMP, 
                ts_created DATETIME DEFAULT CURRENT_TIMESTAMP, 
                PRIMARY KEY (idx_deviceagent), 
                UNIQUE (idx_device, idx_agent), 
                FOREIGN KEY(idx_device) REFERENCES iset_device (idx_device), 
                FOREIGN KEY(idx_agent) REFERENCES iset_agent (idx_agent)
            );""")

            connection.execute("""CREATE TABLE iset_datapoint (
                idx_datapoint BIGINT NOT NULL, 
                idx_deviceagent BIGINT DEFAULT '1' NOT NULL, 
                idx_department BIGINT DEFAULT '1' NOT NULL, 
                idx_billcode BIGINT DEFAULT '1' NOT NULL, 
                id_datapoint BLOB, 
                agent_label BLOB, 
                agent_source BLOB, 
                enabled INTEGER DEFAULT '1', 
                billable INTEGER DEFAULT '0', 
                timefixed_value BLOB, 
                base_type INTEGER DEFAULT '1', 
                last_timestamp BIGINT DEFAULT '0' NOT NULL, 
                ts_modified DATETIME DEFAULT CURRENT_TIMESTAMP, 
                ts_created DATETIME DEFAULT CURRENT_TIMESTAMP, 
                PRIMARY KEY (idx_datapoint), 
                FOREIGN KEY(idx_deviceagent) REFERENCES iset_deviceagent (idx_deviceagent), 
                FOREIGN KEY(idx_department) REFERENCES iset_department (idx_department), 
                FOREIGN KEY(idx_billcode) REFERENCES iset_billcode (idx_billcode), 
                UNIQUE (id_datapoint)
            );""")
            connection.close()
        except sqlite3.Error as e:
            print(str(e))


def _add_engine_pidguard(engine):
    """Add multiprocessing guards.

    Forces a connection to be reconnected if it is detected
    as having been shared to a sub-process.

    source
    ------

    http://docs.sqlalchemy.org/en/latest/faq/connections.html
    "How do I use engines / connections / sessions with
    Python multiprocessing, or os.fork()?"

    Args:
        engine: SQLalchemy engine instance

    Returns:
        None

    """
    @event.listens_for(engine, 'connect')
    def connect(dbapi_connection, connection_record):
        """Get the PID of the sub-process for connections.

        Args:
            dbapi_connection: Connection object
            connection_record: Connection record object

        Returns:
            None

        """
        connection_record.info['pid'] = os.getpid()

    @event.listens_for(engine, 'checkout')
    def checkout(dbapi_connection, connection_record, connection_proxy):
        """Checkout sub-processes connection for sub-processing if needed.

            Checkout is called when a connection is retrieved from the Pool.

        Args:
            dbapi_connection: Connection object
            connection_record: Connection record object
            connection_proxy: Connection proxy object

        Returns:
            None

        """
        # Get PID of main process
        pid = os.getpid()

        # Detect if this is a sub-process
        if connection_record.info['pid'] != pid:
            # substitute log.debug() or similar here as desired
            log_message = (
                'Parent process %s forked (%s) with an open '
                'database connection, '
                'which is being discarded and recreated.'
                '') % (
                    connection_record.info['pid'], pid)
            log.log2debug(1079, log_message)

            connection_record.connection = connection_proxy.connection = None
            raise exc.DisconnectionError(
                "Connection record belongs to pid %s, "
                "attempting to check out in pid %s" %
                (connection_record.info['pid'], pid)
            )


if __name__ == 'infoset.db':
    main()
