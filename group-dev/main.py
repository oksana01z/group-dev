from pyrogram import Client, filters
from pyrogram.types import Message
import config
from quiz import get_question
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


app = Client(
    "quiz_bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    print("/start")
    await message.reply(" Напиши /quiz чтобы начать")

@app.on_message(filters.command("quiz"))
async def quiz_command(client, message):
    text, buttons, question = get_question()
    buttons.append(InlineKeyboardButton("Следующий вопрос ", callback_data="next"))
    await message.reply(
        text,
        reply_markup=InlineKeyboardMarkup([buttons]))


@app.on_callback_query()
async def handle_answer(client, callback_query):
    data = callback_query.data

    if data == "next":
        text, buttons, question = get_question()
        buttons.append(InlineKeyboardButton("Следующий вопрос ", callback_data="next"))
        await callback_query.message.edit_text(
            text,
            reply_markup=InlineKeyboardMarkup([buttons])
        )
        return

    selected_index = int(data)
    text, buttons, question = get_question()
    correct = question["answers"][selected_index]["correct"]

    if correct:
        result = "Правильно"
    else:
        result = "Неправильно"

    await callback_query.answer(result, show_alert=True)

app.run()
