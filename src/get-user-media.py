#!/usr/bin/env python

import json
import os

from PIL import Image
import requests

# https://developers.facebook.com/docs/instagram-basic-display-api/reference/user/media#reading

access_token = os.environ.get('ACCESS_TOKEN')
base_url = 'https://graph.instagram.com/{}/media'
media_id = os.environ.get('USER_ID')


def main():
    url = base_url.format(media_id)
    # https://developers.facebook.com/docs/instagram-basic-display-api/reference/media#fields
    query = {
        'fields': 'username,caption,media_type,media_url,timestamp',
        'access_token': access_token
    }
    response = requests.get(url, params=query)
    print(json.dumps(response.json(), indent=4, sort_keys=True))

    print('username, imageid, caption')
    for item in response.json()['data']:
        print(item['username'], item['id'], item['caption'])
        image_url = item['media_url']
        try:
            with Image.open(requests.get(image_url, stream=True).raw) as im:
                im.show()
        except Exception as e:
            raise e


if __name__ == '__main__':
    main()
