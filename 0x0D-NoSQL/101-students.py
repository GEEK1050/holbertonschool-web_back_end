#!/usr/bin/env python3
"""101-students"""


def top_students(mongo_collection):
    """top_students:
        using mongodb aggregation feature
        to sort projects by average score
    """
    stages = [
        {
            '$group': {
                '_id': 'null',
                'name': '$name',
                'averageScore': {'$avg': '$topics.score'}
            }
        },
        {
            {'$sort': {'averageScore': -1}}
        },
        {
            '$project': {
                '_id': 0
            }
        }
    ]
    mongo_collection.aggregate(stages)
