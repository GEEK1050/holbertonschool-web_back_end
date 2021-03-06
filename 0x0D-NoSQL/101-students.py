#!/usr/bin/env python3
"""101-students"""


def top_students(mongo_collection):
    """top_students:
        using mongodb aggregation feature
        to sort projects by average score
    """
    stages = [
        {
            '$project': {
                'name': '$name',
                'averageScore': {'$avg': '$topics.score'}
            }
        },
        {
            '$sort': {'averageScore': -1}
        }
    ]
    return mongo_collection.aggregate(stages)
