import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Replace 'YOUR_API_TOKEN' with your own bot's API token
bot = telegram.Bot(token='5993868201:AAH1fWq1gRKlIOgF7tW5ME7l29xd1AG7BmU')
updater = Updater(token='5993868201:AAH1fWq1gRKlIOgF7tW5ME7l29xd1AG7BmU', use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm a bot!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def forward(update, context):
    # Replace 'TARGET_CHAT_ID' with the ID of the chat or user you want to forward messages to
    target_chat_id = 'TARGET_CHAT_ID'
    
    # Forward the message to the target chat or user
    context.bot.forward_message(chat_id=target_chat_id, from_chat_id=update.effective_chat.id, message_id=update.message.message_id)

forward_handler = MessageHandler(Filters.text & (~Filters.command), forward)
dispatcher.add_handler(forward_handler)

updater.start_polling()
