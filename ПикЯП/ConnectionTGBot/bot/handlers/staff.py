import os

from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler, CommandHandler, MessageHandler, CallbackQueryHandler
from telegram.ext.filters import TEXT, COMMAND, VIDEO, ALL, CONTACT, Regex

from asgiref.sync import sync_to_async
from ConnectionTGBot.settings import MEDIA_ROOT
from bot.utils.db import get_created_orders, get_keyboard_with_not_accepted_details, add_video, get_client_chat_id


ORDER_STATE, DETAIL_STATE, VIDEO_STATE = range(3)


async def start(update: Update, context: ContextTypes):
    orders = await sync_to_async(get_created_orders)()
    keyboard = [orders[i:i + 3] for i in range(0, len(orders), 3)]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    await update.message.reply_text("Выберите заказ", reply_markup=reply_markup)
    return ORDER_STATE

async def choose_order(update: Update, context: ContextTypes):
    order_number = update.message.text
    context.user_data['order_number'] = order_number
    keyboard = await sync_to_async(get_keyboard_with_not_accepted_details)(order_number)
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(f"Выберите товар!\nЗаказ: {order_number}", reply_markup=reply_markup)
    context.user_data['chat_id'] = update.message.chat_id
    return DETAIL_STATE

async def choose_product(update: Update, context: ContextTypes):
    query = update.callback_query
    context.user_data['detail'] = query.data
    await query.answer()
    await context.bot.send_message(context.user_data['chat_id'], "Теперь жду от вас видео")
    return VIDEO_STATE

async def send_video(update: Update, context: ContextTypes):
    order_detail_pk = context.user_data.get('detail')
    video = update.message.video
    tg_file = await video.get_file()
    local_dir = os.path.join(MEDIA_ROOT,
                              "videos",
                              f"{context.user_data.get('order_number')}",
                              f"{order_detail_pk}")
    file_name = f"{video.file_id}.mp4"
    os.makedirs(local_dir, exist_ok=True)
    local_path = os.path.join(local_dir, file_name)
    await tg_file.download_to_drive(local_path)
    await update.message.reply_text("Я сохранил видео")
    await sync_to_async(add_video)(local_path, order_detail_pk)
    client_chat_id = await sync_to_async(get_client_chat_id)(order_detail_pk)
    await context.bot.send_message(client_chat_id, "Вам видео!")
    return ConversationHandler.END


staff_conversation_handler = ConversationHandler(
    entry_points=[MessageHandler(TEXT & Regex("^Снять видео$"), start)],
    states={
        ORDER_STATE: [MessageHandler(TEXT & Regex("^M-[\d-]*$"), choose_order)],
        DETAIL_STATE: [CallbackQueryHandler(choose_product)],
        VIDEO_STATE: [MessageHandler(VIDEO, send_video)]
    },
    fallbacks=[],
    per_message=False,
)