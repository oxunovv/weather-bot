from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

viloyatlar_btn = ReplyKeyboardMarkup(
    keyboard=
    [
        [KeyboardButton(text="Toshkent"),KeyboardButton(text="Andijon")],
        [KeyboardButton(text="Farg'ona"),KeyboardButton(text="Namangan")],
        [KeyboardButton(text="Samarqand"),KeyboardButton(text="Buxoro")],
        [KeyboardButton(text="Navoiy"),KeyboardButton(text="Qashqadaryo")],
        [KeyboardButton(text="Surxondaryo"),KeyboardButton(text="Xorazm")],
        [KeyboardButton(text="Qoraqalpog‘iston"),KeyboardButton(text="Jizzax")],
        [KeyboardButton(text="Sirdaryo"),KeyboardButton(text="Asaka")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Viloyatni tanlang..."
    )