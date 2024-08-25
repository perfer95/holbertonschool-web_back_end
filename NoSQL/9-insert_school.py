#!/usr/bin/env python3
"""
9. Insert a document in Python
"""


def insert_school(mongo_collection, **kwargs):
    """
    test_2
    """
    document_id = mongo_collection.insert(kwargs)
    return document_id
