#!/usr/bin/env python3
"""
8. List all documents in Python
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection
    Considering that pymongo was imported
    """
    documents = mongo_collection.find()
    if (documents.count() == 0):
        return []
    return list(documents)
