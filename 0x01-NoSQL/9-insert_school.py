#!/usr/bin/env python3
"""insertion"""


def insert_school(mongo_collection, **kwargs):
    """insert to a collection"""
    res = mongo_collection.insert_one(kwargs)
    return res.inserted_id
