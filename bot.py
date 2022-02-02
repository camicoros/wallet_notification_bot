import datetime
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from cat_api import get_cat_image_url
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
                              '/photo - for cat photo'
                              )


def send_photo_command(update, context):
    """ Send photo of cat """
    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.effective_message.message_id)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=get_cat_image_url())


def unknown_command(update, context):
    update.message.reply_text("Sorry, I can't understand this command.")
    help_command(update, context)


def echo(update, context):
    """ Echo the user message"""
    answer = get_bandit_quote()
    if answer:
        update.message.reply_text(answer)
    else:
        update.message.reply_text(get_list_of_emoji())


def error(update, context):
    """ Log errors caused by updates """
    logger.warning('Update "%s" caused error "%s', update, context.error)


def main():
    updater = Updater("5246885222:AAFlooXyDTJFapnfdvIrYVgc-1RowSpLuoM", use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("photo", send_photo_command))
    dp.add_handler(MessageHandler(Filters.command, unknown_command))

    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()


if __name__ == '__main__':
    main()
