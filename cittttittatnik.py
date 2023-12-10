import random
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler



def start(update, context):
    reply_keyboard = [['Quote']]
    update.message.reply_text(
        'Привет! Я телеграм бот-цитатник. Нажми на кнопку "Quote", чтобы получить случайную цитату.',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )


def get_quote(update, context):
    quotes = [
        'Стремитесь не к успеху, а к ценностям, которые он дает. Альберт Эйнштейн',
        'Сложнее всего начать действовать, все остальное зависит только от упорства. Амелия Эрхарт',
        'Логика может привести Вас от пункта А к пункту Б, а воображение — куда угодно.Альберт Эйнштейн',
        'Начинать всегда стоит с того, что сеет сомнения.Борис Стругацкий',
        'Наука — это организованные знания, мудрость — это организованная жизнь .Иммануил Кант',
        'Вы никогда не пересечете океан, если не наберетесь мужества потерять берег из виду. Христофор Колумб',
        ' Два самых важных дня в твоей жизни: день, когда ты появился на свет, и день, когда понял, зачем. Марк Твен',
        'Есть только один способ избежать критики: ничего не делайте, ничего не говорите и будьте никем. Аристотель',
        ' Стоит только поверить, что вы можете – и вы уже на полпути к цели.',
    ]
    quote = random.choice(quotes)
    update.message.reply_text(quote)



def unknown(update, context):
    update.message.reply_text("Извините, я не понимаю эту команду.")



def main():
    updater = Updater('6703775474:AAFvLw9Uk-um8CbRQ_Rq_3uuWc-qQHmz1hw', use_context=True)

    dispatcher = updater.dispatcher


    dispatcher.add_handler(CommandHandler('start', start))


    dispatcher.add_handler(MessageHandler(Filters.regex('^Quote$'), get_quote))


    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
