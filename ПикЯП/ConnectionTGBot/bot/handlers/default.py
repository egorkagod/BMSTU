from asgiref.sync import sync_to_async
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup
from telegram.constants import InlineKeyboardButtonLimit
from telegram.ext import ContextTypes
from bot.utils.db import get_user_details


async def default_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Если потерялись жмите /help')


async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_details = await get_user_details(chat_id=update.effective_chat.id)
    access = user_details.get('access')
    if access == 'client':
        await update.message.reply_text('Возможности клиента')
    elif access == 'staff':
        keyboard = [
            ['Снять видео']
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        await update.message.reply_text('Выберите действие', reply_markup=reply_markup)
    else:
        await update.message.reply_text('Пожалуйста зарегистрируйтесь /start')