from telegram.ext import (
    CommandHandler,
    MessageHandler,
    ContextTypes,
)
from telegram.ext.filters import ALL
from .config import application
from bot.handlers.default import default_handler, help_handler

from .handlers.start import start_conversation_handler
from .handlers.staff import staff_conversation_handler

# Handlers
application.add_handler(CommandHandler('help', help_handler))
application.add_handler(start_conversation_handler)
application.add_handler(staff_conversation_handler)
application.add_handler(MessageHandler(ALL, default_handler))