import json
import requests
from flask import current_app
from flask_babel import _


def translate(text, dest_language):
    if 'MS_TRANSLATOR_KEY' not in current_app.config or \
            not current_app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    params = {'api-version': '3.0',
              'to': dest_language}
    headers = {'Ocp-Apim-Subscription-Key': current_app.config['MS_TRANSLATOR_KEY'],
               'Content-Type': 'application/json; charset=UTF-8'}
    body = [{'Text': text}]
    response = requests.post(
        'https://api.cognitive.microsofttranslator.com/translate',
        params=params, headers=headers, json=body)
    if response.status_code != 200:
        return _('Error: the translation service failed.')
    return json.loads(response.content.decode('utf-8-sig'))
