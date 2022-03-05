import requests
import json


def get_fox_image_url():
    url = 'https://randomfox.ca/floof/'
    headers = {
        'Content-Type': 'application/json',
    }
    r = requests.get(url, headers=headers)

    success_url = None
    if r.status_code in range(200, 230):
        text = json.loads(r.text)
        if text.get('image'):
            success_url = str(text.get('image')).replace("\\", "")

    return success_url


def main():
    print(get_fox_image_url())


if __name__ == '__main__':
    main()
