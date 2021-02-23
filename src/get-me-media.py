#!/usr/bin/env python

import os

import requests

# https://developers.facebook.com/docs/instagram-basic-display-api/guides/getting-profiles-and-media

access_token = os.environ.get('ACCESS_TOKEN')
base_url = 'https://graph.instagram.com/me/media'


def main():
    query = {'fields': 'id,caption', 'access_token': access_token}
    response = requests.get(base_url, params=query)
    print(response.url)
    print(response.json())


if __name__ == '__main__':
    main()
