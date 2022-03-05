import logging
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from cat_api import get_cat_image_url
from dog_api import get_dog_image_url
from emoji.utils import get_list_of_emoji
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
                              '/cat_photo - for cat photo\n'
                              '/dog_photo - for dog photo\n'
                              )


def send_cat_photo_command(update, context):
    """ Send photo of cat """
    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.effective_message.message_id)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=get_cat_image_url())


def send_dog_photo_command(update, context):
    """ Send photo of dog """
    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.effective_message.message_id)
    # context.bot.send_photo(chat_id=update.effective_chat.id, photo=get_dog_image_url())


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
    dp.add_handler(CommandHandler("cat_photo", send_cat_photo_command))
    dp.add_handler(CommandHandler("dog_photo", send_dog_photo_command))
    dp.add_handler(MessageHandler(Filters.command, unknown_command))

    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()


if __name__ == '__main__':
    main()
