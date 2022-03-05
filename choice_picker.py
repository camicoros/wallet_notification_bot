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
    return result[0] if len(result) else None


if __name__ == "__main__":
    print(make_a_choice(
        population=[EMOJI, PHOTO],
        weights=[0.8, 0.2]
    ))
