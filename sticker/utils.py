import random
import itertools

from sticker.codes import PIG_STICKER_IDS

result_list = [
    PIG_STICKER_IDS,
]

COMMON_LIST = list(set(itertools.chain(*result_list)))


def get_random_sticker():
    return random.choice(COMMON_LIST)


def get_pig_sticker():
    return random.choice(PIG_STICKER_IDS)


def main():
    print(get_random_sticker())
    print(get_pig_sticker())


if __name__ == "__main__":
    main()
