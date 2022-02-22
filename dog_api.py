import requests
import json


def get_dog_image_url():
    url = 'https://dog.ceo/api/breeds/image/random'
    headers = {
        'Content-Type': 'application/json',
    }
    r = requests.get(url, headers=headers)

    success_url = None
    if r.status_code in range(200, 230):
        text = json.loads(r.text)
        if text.get('status') == 'success':
            success_url = text.get('message', None)

    return success_url


def main():
    print(get_dog_image_url())


if __name__ == '__main__':
    main()
