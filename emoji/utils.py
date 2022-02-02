import random
import itertools

from emoji.codes import RGI_EMOJI_MODIFIER_SEQUENCE, RGI_EMOJI_TAG_SEQUENCE, RGI_EMOJI_FLAG_SEQUENCE, \
    EMOJI_KEYCAP_SEQUENCE, BASIC_EMOJI

result_list = [
    RGI_EMOJI_MODIFIER_SEQUENCE,
    RGI_EMOJI_TAG_SEQUENCE,
    RGI_EMOJI_FLAG_SEQUENCE,
    EMOJI_KEYCAP_SEQUENCE, BASIC_EMOJI
]

COMMON_LIST = list(set(itertools.chain(*result_list)))


def get_random_emoji():
    return random.choice(COMMON_LIST)


def get_list_of_emoji(start=0, end=5):
    return "".join(random.choices(COMMON_LIST, k=random.randint(start, end)))


def main():
    print(get_random_emoji())
    print(get_list_of_emoji())


if __name__ == "__main__":
    main()
