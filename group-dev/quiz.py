import json
import random
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_question():
    with open("questions.json", "r", encoding="utf-8") as f:
        questions = json.load(f)
    question = random.choice(questions)
    text = question["question"]
    buttons = [
        InlineKeyboardButton(a["text"], callback_data=str(i))
        for i, a in enumerate(question["answers"])
    ]
    return text, buttons, question
