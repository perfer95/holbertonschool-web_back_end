#!/usr/bin/env python3
"""
8. List all documents in Python
"""
import pymongo


def list_all(mongo_collection):
    """
    Python function that lists all documents in a collection
    """
    docs = mongo_collection.find()
    if docs.count() == 0:
        return []
    return docs

if __name__ == "__main__":
    pass
