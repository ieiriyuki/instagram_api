#!/usr/bin/env python

import json
import os

from PIL import Image
import requests

# https://developers.facebook.com/docs/instagram-basic-display-api/guides/getting-profiles-and-media

access_token = os.environ.get('ACCESS_TOKEN')
base_url = 'https://graph.instagram.com/{}'
media_id = os.environ.get('MEDIA_ID')


def main():
    url = base_url.format(media_id)
    # https://developers.facebook.com/docs/instagram-basic-display-api/reference/media#fields
    query = {
        'fields': 'username,caption,media_type,media_url,permalink,timestamp',
        'access_token': access_token
    }
    response = requests.get(url, params=query)
    print(json.dumps(response.json(), indent=4, sort_keys=True))

    image_url = response.json()['media_url']
    try:
        with Image.open(requests.get(image_url, stream=True).raw) as im:
            im.show()
    except Exception as e:
        raise e


if __name__ == '__main__':
    main()
