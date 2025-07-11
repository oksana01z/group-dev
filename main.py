from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from quiz import get_question
from database import get_user_score, add_score
