import argparse
import logging
import os
from dotenv import load_dotenv
from urllib.parse import urlparse

import requests

load_dotenv()


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--link")
    return parser


def is_bitlink(url, domain):
    parsed = urlparse(url)
    return True if parsed.netloc == domain else False


def get_netloc_with_path(url):
    parsed = urlparse(url)
    return f"{parsed.netloc}{parsed.path}"


def is_valid_url(url):
    response = requests.get(url)
    response.raise_for_status()


def get_shorten(token, link, domain):
    url = r"https://api-ssl.bitly.com/v4/shorten"
    headers = {"Authorization": f"Bearer {token}"}
    data = {"long_url": link, "domain": domain}
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()["link"]


def get_clicks(token, bitlink):
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]


def main():
    parser = create_parser()
    namespace = parser.parse_args()
    bitly_token = os.environ["BITLY_TOKEN"]
    custom_domain = os.getenv("CUSTOM_DOMAIN")
    logging.basicConfig(level=logging.INFO)
    url = namespace.link
    is_valid_url(url)
    domain = custom_domain if custom_domain else "bit.ly"
    if is_bitlink(url, domain):
        bitlink = get_netloc_with_path(url)
        print("Your bitlink clicks: ", end="")
        print(get_clicks(bitly_token, bitlink))
    else:
        print("Your link is: ", end="")
        print(get_shorten(bitly_token, url, domain))


if __name__ == "__main__":
    main()
