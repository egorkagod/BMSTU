from asgiref.sync import sync_to_async

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from bot.models import Staff, Client, Order, OrderDetail, Video


async def get_user_details(**filters):
    access = None
    user = None
    if staff := await sync_to_async(Staff.objects.filter(**filters).first)():
        access = "staff"
        user = staff
    elif client := await sync_to_async(Client.objects.filter(**filters).first)():
        access = "client"
        user = client
    return {"access": access, "user": user}

def get_created_orders():
    return list(map(str, Order.objects.filter(status="CREATED")))

def get_keyboard_with_not_accepted_details(order_number):
    order = Order.objects.get(number=order_number)
    details = order.details.filter(is_accepted=False)
    keyboard = []
    for detail in details:
        keyboard.append([InlineKeyboardButton(detail.name, callback_data=detail.pk)])
    return keyboard

def add_video(path, detail_pk):
    Video.objects.create(path=path, order_detail_id=detail_pk)

def get_client_chat_id(detail_pk):
    order_detail = OrderDetail.objects.get(pk=detail_pk)
    client = order_detail.order.client
    client_chat_id = client.chat_id
    return client_chat_id