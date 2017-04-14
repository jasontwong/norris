import json
import os
import random
import logging
import urlparse
import sys
sys.path.append('vendored')
from algoliasearch import algoliasearch


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def _getJokes(query):
    client = algoliasearch.Client(
        os.environ['ALGOLIA_APP_ID'],
        os.environ['ALGOLIA_API_KEY']
    )

    jokes = client.init_index('jokes')

    return jokes.search(query)


def _getQuery(event):
    body = event.get('body') or 'text='
    params = urlparse.parse_qs(body, True)
    logger.info('got params{}'.format(params))

    return params['text'].pop()


def norris(event, context):
    query = _getQuery(event)
    results = _getJokes(query)
    item = random.choice(results['hits'])
    body = {
        'response_type': 'in_channel',
        'text': item['joke']
    }

    response = {
        'statusCode': 200,
        'body': json.dumps(body)
    }

    return response
