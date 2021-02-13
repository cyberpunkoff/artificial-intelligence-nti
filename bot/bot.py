from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler, ConversationHandler
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from worker import *
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
FIRST, SECOND, THIRD, END, START = range(5)

mdata = {} 


def start(update: Update, context: CallbackContext) -> None:

    
    
    keyboard = [[InlineKeyboardButton("Программирование и разработка", callback_data='programming')],
        [InlineKeyboardButton("Информационная безопасность", callback_data='security')],
        [InlineKeyboardButton("Искуственный интеллект и обработка данных", callback_data='ai_and_data')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text('Привет! Моя цель - выдавать вам статьи сайта habr.com\nПожалуйста, учитывайте, что я нахожусь в глубокой стадии разработки!')
    update.message.reply_text('Давайте начнем? Расскажите, какая из предложенных тем нравится вам больше всего:', reply_markup=reply_markup)
    
    return FIRST
    
def start_over(update: Update, context: CallbackContext) -> None:

    keyboard = [[InlineKeyboardButton("Программирование и разработка", callback_data='programming')],
        [InlineKeyboardButton("Информационная безопасность", callback_data='security')],
        [InlineKeyboardButton("Искуственный интеллект и обработка данных", callback_data='ai_and_data')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query = update.callback_query
    query.answer()
    query.edit_message_text('Какая из предложенных тем нравится вам больше всего:', reply_markup=reply_markup)
    
    return FIRST

def get_stype(update: Update, context: CallbackContext) -> None:

    query = update.callback_query
    mdata["prefered"] = query.data 
    query.answer()
    
    keyboard = [
        [
            InlineKeyboardButton("Популярную", callback_data="caual"),
            InlineKeyboardButton("Необычную", callback_data="unusual"),
            InlineKeyboardButton("Среднее", callback_data="usual"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query.edit_message_text("Какую вы хотите статью?", reply_markup=reply_markup)

    return SECOND

def get_lenght(update: Update, context: CallbackContext) -> None:

    query = update.callback_query
    mdata["stype"] = query.data
    query.answer()
    
    keyboard = [
        [
            InlineKeyboardButton("Много", callback_data="higer"),
            InlineKeyboardButton("Немного", callback_data="lower"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query.edit_message_text("Сколько у вас времени на прочтение?", reply_markup=reply_markup)
    
    return THIRD

def choose(update: Update, context: CallbackContext) -> None:

    query = update.callback_query
    mdata["lenght"] = query.data
    query.answer()
    
    query.edit_message_text(recommend(mdata["prefered"], mdata["stype"], mdata["lenght"]))
    
    keyboard = [
        [
            InlineKeyboardButton("Еще одну", callback_data="more"),
            InlineKeyboardButton("Хватит", callback_data="enough"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query.message.reply_text("Хотите еще одну статью?", reply_markup=reply_markup)
    
    return END

def end(update: Update, context: CallbackContext) -> None:

    query = update.callback_query
    query.answer()
    query.message.reply_text(text="Спасибо за уделенное мне время! Приходите еще.\n\nP.s. если вам захочется получить еще одну статью введите команду /start")
    
    return ConversationHandler.END

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Отправьте /start для начала использования')

def main():

    updater = Updater("TOKEN")
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            
            FIRST: [
                CallbackQueryHandler(get_stype)
            ],
            SECOND: [
                CallbackQueryHandler(get_lenght)
            ],
            THIRD: [
                CallbackQueryHandler(choose)
            ],
            END: [
                CallbackQueryHandler(start_over, pattern = "^more$"),
                CallbackQueryHandler(end, pattern = "^enough$")
            ],
        },
        fallbacks=[CommandHandler('start', start)],
    )

    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()