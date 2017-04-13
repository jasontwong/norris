import json
import os
import random
import sys
sys.path.append('vendored')
from algoliasearch import algoliasearch


def _getJokes(query):
    client = algoliasearch.Client(
        os.environ['ALGOLIA_APP_ID'],
        os.environ['ALGOLIA_API_KEY']
    )

    jokes = client.init_index('jokes')

    return jokes.search(query)


def norris(event, context):
    query_params = event.get('queryStringParameters') or {}
    query = query_params.get('q', '')
    results = _getJokes(query)
    item = random.choice(results['hits'])
    body = {
        'joke': item['joke']
    }

    response = {
        'statusCode': 200,
        'body': json.dumps(body)
    }

    return response
