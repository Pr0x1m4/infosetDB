#!/usr/bin/env python3
"""Infoset ORM classes.

Manages connection pooling among other things.

"""

# SQLobject stuff
from sqlalchemy import UniqueConstraint, PrimaryKeyConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.sqlite import DATETIME, INTEGER
from sqlalchemy.dialects.sqlite import NUMERIC, BLOB
from sqlalchemy import Column, String
from sqlalchemy import ForeignKey
from infoset.db import POOL, ENGINE
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)
import os

SESSION = scoped_session(POOL)

BASE = declarative_base()
BASE.metadata.bind = ENGINE

BASE.query = SESSION.query_property()


class Device(BASE):
    """Class defining the iset_device table of the database."""

    __tablename__ = 'iset_device'
    __table_args__ = (

        UniqueConstraint(
            'devicename'),
        {
            'mysql_engine': 'InnoDB'
        }
    )

    idx_device = Column(
        INTEGER(), primary_key=True,
        autoincrement=True)

    devicename = Column(String, nullable=True, default=None)  # BLOB

    description = Column(String, nullable=True, default=None)  # BLOB

    enabled = Column(INTEGER(), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class DeviceAgent(BASE):
    """Class defining the iset_deviceagent table of the database."""

    __tablename__ = 'iset_deviceagent'
    __table_args__ = (
        UniqueConstraint(
            'idx_device', 'idx_agent'),
        {
            'mysql_engine': 'InnoDB'
        }
    )

    idx_deviceagent = Column(
        INTEGER(), primary_key=True,
        autoincrement=True)

    idx_device = Column(
        INTEGER(), ForeignKey('iset_device.idx_device'),
        nullable=False, server_default='1')

    idx_agent = Column(
        INTEGER(), ForeignKey('iset_agent.idx_agent'),
        nullable=False, server_default='1')

    enabled = Column(INTEGER(), server_default='1')

    last_timestamp = Column(
        INTEGER(), nullable=False, server_default='0')

    ts_modified = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class Data(BASE):
    """Class defining the iset_data table of the database."""

    __tablename__ = 'iset_data'
    __table_args__ = (
        PrimaryKeyConstraint(
            'idx_datapoint', 'timestamp'),
        {
            'mysql_engine': 'InnoDB'
        }
    )

    idx_datapoint = Column(
        INTEGER(), ForeignKey('iset_datapoint.idx_datapoint'),
        server_default='1')

    timestamp = Column(INTEGER(), nullable=False, default='1')

    value = Column(NUMERIC(40, 10), default=None)


class Agent(BASE):
    """Class defining the iset_agent table of the database."""

    __tablename__ = 'iset_agent'
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }

    idx_agent = Column(
        INTEGER(), primary_key=True,
        autoincrement=True)

    idx_agentname = Column(
        INTEGER(), ForeignKey('iset_agentname.idx_agentname'),
        nullable=False, server_default='1')

    id_agent = Column(String, unique=True, nullable=True, default=None)  # BLOB

    enabled = Column(INTEGER(), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class AgentName(BASE):
    """Class defining the iset_agentname table of the database."""

    __tablename__ = 'iset_agentname'
    __table_args__ = (
        UniqueConstraint(
            'name'),
        {
            'mysql_engine': 'InnoDB'
        }
    )

    idx_agentname = Column(
        INTEGER(), primary_key=True,
        autoincrement=True)

    name = Column(String, nullable=True, default=None)  # BLOB

    enabled = Column(INTEGER(), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class Datapoint(BASE):
    """Class defining the iset_datapoint table of the database."""

    __tablename__ = 'iset_datapoint'
    __table_args__ = (
        {
            'mysql_engine': 'InnoDB'
        }
    )

    idx_datapoint = Column(
        INTEGER(), primary_key=True,
        autoincrement=True)

    idx_deviceagent = Column(
        INTEGER(), ForeignKey('iset_deviceagent.idx_deviceagent'),
        server_default='1')

    idx_department = Column(
        INTEGER(), ForeignKey('iset_department.idx_department'),
        server_default='1')

    idx_billcode = Column(
        INTEGER(), ForeignKey('iset_billcode.idx_billcode'),
        server_default='1')

    id_datapoint = Column(
        INTEGER(), unique=True, nullable=True, default=None)

    agent_label = Column(INTEGER(), nullable=True, default=None)

    agent_source = Column(INTEGER(), nullable=True, default=None)

    enabled = Column(INTEGER(), server_default='1')

    billable = Column(INTEGER(), server_default='0')

    timefixed_value = Column(INTEGER(), nullable=True, default=None)

    base_type = Column(INTEGER(), server_default='1')

    last_timestamp = Column(
        INTEGER(), nullable=False, server_default='0')

    ts_modified = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class Department(BASE):
    """Class defining the iset_department table of the database."""

    __tablename__ = 'iset_department'
    __table_args__ = (
        UniqueConstraint(
            'code'),
        {
            'mysql_engine': 'InnoDB'
        }
    )

    idx_department = Column(
        INTEGER(), primary_key=True,
        autoincrement=True, nullable=False)

    code = Column(BLOB, nullable=True, default=None)

    name = Column(BLOB, nullable=True, default=None)

    enabled = Column(INTEGER(), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class Billcode(BASE):
    """Class defining the iset_billcode table of the database."""

    __tablename__ = 'iset_billcode'
    __table_args__ = (
        UniqueConstraint(
            'code'),
        {
            'mysql_engine': 'InnoDB'
        }
    )

    idx_billcode = Column(
        INTEGER(), primary_key=True,
        autoincrement=True, nullable=False)

    code = Column(BLOB, nullable=True, default=None)

    name = Column(BLOB, nullable=True, default=None)

    enabled = Column(INTEGER(), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class Configuration(BASE):
    """Class defining the iset_configuration table of the database."""

    __tablename__ = 'iset_configuration'
    __table_args__ = (
        UniqueConstraint(
            'config_key'),
        {
            'mysql_engine': 'InnoDB'
        }
    )

    idx_configuration = Column(
        INTEGER(), primary_key=True,
        autoincrement=True, nullable=False)

    config_key = Column(BLOB, nullable=True, default=None)

    config_value = Column(BLOB, nullable=True, default=None)

    enabled = Column(INTEGER(), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))
