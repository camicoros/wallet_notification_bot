import random


EMOJI = "emoji"
PHOTO = "photo"
STICKER = "sticker"


def make_a_choice(population, weights):
    result = random.choices(
        population=population,
        weights=weights,
        k=1,
    )
    return result
