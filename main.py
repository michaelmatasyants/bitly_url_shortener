import requests
from urllib.parse import urlsplit
from dotenv import load_dotenv
from dotenv import find_dotenv
import os
import argparse


def shorten_link(token, link):
    url = 'https://api-ssl.bitly.com/v4'
    headers = {
      "Authorization": f'Bearer {token}',
    }
    payload = {'long_url': link}
    response_short = requests.post(f'{url}/bitlinks',
                                   headers=headers,
                                   json=payload)
    response_short.raise_for_status()
    bitlink = response_short.json()["link"]
    return bitlink


def count_clicks(token, link):
    parsed_url = urlsplit(link)
    bitlink = f'{parsed_url.netloc}{parsed_url.path}'
    url = 'https://api-ssl.bitly.com/v4'
    headers = {
      'Authorization': f'Bearer {token}',
    }
    params = {'unit': 'day', 'units': '-1'}
    count_clicks_response = requests.get(
        f'{url}/bitlinks/{bitlink}/clicks/summary',
        params=params, headers=headers
        )
    count_clicks_response.raise_for_status()
    return count_clicks_response.json()["total_clicks"]


def is_bitlink(token, link):
    url = 'https://api-ssl.bitly.com/v4'
    headers = {'Authorization': f'Bearer {token}'}
    parsed_url = urlsplit(link)
    bitlink = f'{parsed_url.netloc}{parsed_url.path}'
    bitlink_response = requests.get(f'{url}/bitlinks/{bitlink}',
                                    headers=headers)
    return bitlink_response.ok


def main():
    load_dotenv(find_dotenv())
    token = os.environ['BITLY_TOKEN']
    parser = argparse.ArgumentParser(
        description="Shortening link or geting count of clicks on the bitlink"
        )
    parser.add_argument("link", help="bitlink or a link for shortening")
    args = parser.parse_args()
    user_input = args.link
    if is_bitlink(token, user_input):
        print(f'Count of clicks on {user_input} is:',
              count_clicks(token, user_input))
    else:
        try:
            requests.get(user_input).raise_for_status()
            print(f'Your shortened link for {user_input} is:',
                  shorten_link(token, user_input))
        except requests.HTTPError as http_err:
            print(f'HTTP error occured: {http_err}')
        except Exception as err:
            print(f'Other error occured: {err}')


if __name__ == '__main__':
    main()
