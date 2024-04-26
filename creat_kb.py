from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button = InlineKeyboardButton("авторизоваться", callback_data="start")
    keyboard.add(button)
    return keyboard


def q_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button = InlineKeyboardButton("question", callback_data="question")
    kb.add(button)
    return kb


def ret_prof_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button = InlineKeyboardButton("cancel", callback_data="ret_prof")
    kb.add(button)
    return kb


def question() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = InlineKeyboardButton("next", callback_data="next_q")
    button2 = InlineKeyboardButton("prev", callback_data="prev_q")
    kb.add(button2, button1)
    return kb


def question_2() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = InlineKeyboardButton("next", callback_data="next_q")
    button2 = InlineKeyboardButton("prev", callback_data="prev_q")
    button3 = InlineKeyboardButton("finish", callback_data="finish_q")
    kb.add(button2, button1).add(button3)
    return kb
