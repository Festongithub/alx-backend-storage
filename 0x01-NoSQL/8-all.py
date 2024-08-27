#!/usr/bin/env python3
"""lists all documents """


def list_all(mongo_collection):
    """list collections"""
    docs = mongo_collection.find()

    if docs.count() == 0:
        return []

    return docs
