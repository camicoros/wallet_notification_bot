import requests
import json


def get_cat_image_url():
    url = 'https://api.thecatapi.com/v1/images/search?format=json'
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': '125ef3b4-f410-44ff-acd0-7ae737be7f6a',
    }
    r = requests.get(url, headers=headers)

    success_url = None
    if r.status_code in range(200, 230):
        try:
            text = json.loads(r.text)
            if isinstance(text, list):
                success_url = text[0].get('url', None)
            elif isinstance(text, dict):
                success_url = text.get('url', None)
        except Exception as e:
            print(e)

    return success_url


def main():
    print(get_cat_image_url())


if __name__ == '__main__':
    main()
