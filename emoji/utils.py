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


def get_dog_emoji():
    dogs = [u"\uE052", u"\U0001F415"]
    return random.choice(dogs)


def get_cat_emoji():
    cats = [
        u"\uE04F",  # cat face
        u"\U0001F408",  # cat
        u"\U0001F63B",  # heart_eyes_cat
        u"\U0001F63C",  # smirk_cat
        u"\U0001F638",  # smile_cat
        u"\U0001F639",  # joy_cat
        u"\U0001F63A",  # smiley_cat
        u"\U0001F63F",  # crying_cat_face
        u"\U0001F640",  # scream_cat
        u"\U0001F63E",  # pouting_cat
        u"\U0001F63D",  # kissing_cat
    ]
    return random.choice(cats)


def get_pig_emoji():
    pigs = [
        u"\U0001F43D",  # pig_nose
        u"\uE10B",  # pig_face
        u"\U0001F416",  # pig
    ]
    return random.choice(pigs)


def get_fox_emoji():
    return u"\U0001F98A"


def get_list_of_emoji(start=0, end=2):
    return "".join(random.choices(COMMON_LIST, k=random.randint(start, end)))


def main():
    print(get_dog_emoji())
    print(get_cat_emoji())
    print(get_pig_emoji())
    print(get_fox_emoji())
    print(get_random_emoji())
    print(get_list_of_emoji())


if __name__ == "__main__":
    main()
