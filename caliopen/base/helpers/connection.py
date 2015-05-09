# -*- coding: utf-8 -*-
"""Caliopen storage session helpers."""

from cqlengine.connection import setup as setup_cassandra
from caliopen.base.config import Configuration


def connect_storage():
    """Connect to storage engines."""
    setup_cassandra(Configuration('global').get('cassandra.hosts'),
                    Configuration('global').get('cassandra.keyspace'),
                    Configuration('global').get('cassandra.consistency_level'))