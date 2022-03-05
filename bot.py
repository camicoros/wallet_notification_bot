import logging
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from cat_api import get_cat_image_url
from dog_api import get_dog_image_url
from fox_api import get_fox_image_url
from emoji.utils import get_list_of_emoji, get_cat_emoji, get_dog_emoji, get_fox_emoji, get_pig_emoji
from sticker.utils import get_pig_sticker
from choice_picker import make_a_choice, EMOJI, STICKER, PHOTO
from stalker_bandit import get_bandit_quote

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def start_command(update, context):
    """ Send a message when /start """
    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.effective_message.message_id)
    update.message.reply_text('Hi, boss!')


def help_command(update, context):
    """ Send a message when /help """
    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.effective_message.message_id)
    update.message.reply_text(''
                              'Here what I can do for you, boss!\n\n'
                              '/start - for start\n'
                              '/help - for help\n'
                              f'/cat - for cat {get_cat_emoji()}\n'
                              f'/dog - for dog {get_dog_emoji()}\n'
                              f'/fox - for fox {get_fox_emoji()}\n'
                              f'/pig - for pig {get_pig_emoji()}\n'
                              )


def send_cat_command(update, context):
    """ Send photo of cat """
    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.effective_message.message_id)
    result = make_a_choice(
        population=[
            EMOJI,
            PHOTO,
        ],
        weights=[
            0.8,
            0.2,
        ]
    )
    if result == EMOJI:
        context.bot.send_message(chat_id=update.effective_chat.id, text=get_cat_emoji())
    elif result == PHOTO:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=get_cat_image_url())
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="MEOW-MEOW! ^3^")


def send_dog_command(update, context):
    """ Send photo of dog """
    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.effective_message.message_id)
    result = make_a_choice(
        population=[
            EMOJI,
            PHOTO,
        ],
        weights=[
            0.8,
            0.2,
        ]
    )
    if result == EMOJI:
        context.bot.send_message(chat_id=update.effective_chat.id, text=get_dog_emoji())
    elif result == PHOTO:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=get_dog_image_url())
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="WOOF-WOOF!!!")


def send_fox_command(update, context):
    """ Send photo of fox """
    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.effective_message.message_id)
    result = make_a_choice(
        population=[
            EMOJI,
            PHOTO,
        ],
        weights=[
            0.8,
            0.2,
        ]
    )
    if result == EMOJI:
        context.bot.send_message(chat_id=update.effective_chat.id, text=get_fox_emoji())
    elif result == PHOTO:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=get_fox_image_url())
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="FUR-FUR-FUR <3")


def send_pig_command(update, context):
    """ Send photo of pig """
    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.effective_message.message_id)
    result = make_a_choice(
        population=[
            EMOJI,
            STICKER,
        ],
        weights=[
            0.5,
            0.5,
        ]
    )
    if result == EMOJI:
        context.bot.send_message(chat_id=update.effective_chat.id, text=get_pig_emoji())
    elif result == STICKER:
        context.bot.send_sticker(chat_id=update.effective_chat.id, sticker=get_pig_sticker())
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="ХРЮ-ХРЮ! {>(**)<}")


def unknown_command(update, context):
    update.message.reply_text("Sorry, I can't understand this command.")
    help_command(update, context)


def echo(update, context):
    """ Echo the user message"""
    answer = get_bandit_quote() or get_list_of_emoji()
    if answer:
        update.message.reply_text(answer)


def error(update, context):
    """ Log errors caused by updates """
    logger.warning('Update "%s" caused error "%s', update, context.error)


def main():
    updater = Updater(os.environ['SECRET_KEY'], use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("cat", send_cat_command))
    dp.add_handler(CommandHandler("dog", send_dog_command))
    dp.add_handler(CommandHandler("fox", send_fox_command))
    dp.add_handler(CommandHandler("pig", send_pig_command))
    dp.add_handler(MessageHandler(Filters.command, unknown_command))

    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()


if __name__ == '__main__':
    main()
