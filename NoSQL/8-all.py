#!/usr/bin/python3
"""
8. List all documents in Python
"""


def list_all(mongo_collection):
    """
    Python function that lists all documents in a collection
    """
    docs = mongo_collection.find()
    if docs.count() == 0:
        return []
    return docs
