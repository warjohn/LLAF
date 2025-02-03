from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, CallbackGame

from routers.utils.data import DataStorage


def key_start():
    storage = DataStorage()
    start_button_text, _, _, _ = storage.get_columns()
    print("start_button_text", start_button_text)

    default_buttons = ["Hot sales", "About us", "Wanna buy", "Product Expert", "Contact the manager", "our products"]

    if not start_button_text:
        # Если список пустой, используем стандартные кнопки
        menu = [
             [InlineKeyboardButton(text=default_buttons[1], callback_data="_", url="https://telegra.ph/LUKOIL-Lubricants-Africa-10-09")],
             [InlineKeyboardButton(text=default_buttons[5], callback_data="_",
                                  url="https://telegra.ph/LUKOIL-PRODUCTS-10-17")],
             [InlineKeyboardButton(text=default_buttons[2], callback_data="buy")],
             [InlineKeyboardButton(text=default_buttons[3], callback_data="saler")],
             [InlineKeyboardButton(text=default_buttons[4], callback_data="_", url="https://t.me/seshcha")],
             [InlineKeyboardButton(text=default_buttons[0], callback_data="hot_sales")]
        ]
    else:
        # Используем значения из start_button_text, а если их недостаточно, берем из default_buttons
        menu = [
            [InlineKeyboardButton(text=start_button_text[1] if len(start_button_text) > 1 else default_buttons[1],
                                  callback_data="_", url = "https://telegra.ph/LUKOIL-Lubricants-Africa-10-09")],
            [InlineKeyboardButton(text=start_button_text[5] if len(start_button_text) > 5 else default_buttons[5],
                                  callback_data="_", url="https://telegra.ph/LUKOIL-PRODUCTS-10-17")],
            [InlineKeyboardButton(text=start_button_text[2] if len(start_button_text) > 2 else default_buttons[2],
                                  callback_data="buy")],
            [InlineKeyboardButton(text=start_button_text[3] if len(start_button_text) > 3 else default_buttons[3],
                                  callback_data="saler")],
            [InlineKeyboardButton(text=start_button_text[4] if len(start_button_text) > 4 else default_buttons[4],
                                  callback_data="_", url="https://t.me/seshcha")],
            [InlineKeyboardButton(text=start_button_text[0] if len(start_button_text) > 0 else default_buttons[0],
                                  callback_data="hot_sales")],
        ]

    menu_key = InlineKeyboardMarkup(inline_keyboard=menu, resize_keyboard=True, one_time_keyboard=True)

    return menu_key


def about_us_key():
    storage = DataStorage()
    _, aboutUS_button_text, _, _ = storage.get_columns()
    print("aboutUS_button_text", aboutUS_button_text)

    # Значения по умолчанию
    default_buttons = [
        "Link to site",
        "Linked IN",
        "Instagram"
    ]

    if not aboutUS_button_text:
        # Если список пустой, используем стандартные кнопки
        about_us = [
            [InlineKeyboardButton(text=default_buttons[0], callback_data="_",
                                  url="https://wiki.ssmu.ru/index.php?title=%D0%94%D0%BE%D0%B1%D1%80%D0%BE_%D0%BF%D0%BE%D0%B6%D0%B0%D0%BB%D0%BE%D0%B2%D0%B0%D1%82%D1%8C_%D0%B2_%D0%AD%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D0%BD%D1%83%D1%8E_%D1%8D%D0%BD%D1%86%D0%B8%D0%BA%D0%BB%D0%BE%D0%BF%D0%B5%D0%B4%D0%B8%D1%8E_%D0%A1%D0%B8%D0%B1%D0%93%D0%9C%D0%A3")],
            [InlineKeyboardButton(text=default_buttons[1], callback_data="link")],
            [InlineKeyboardButton(text=default_buttons[2], callback_data="inst")],
            [InlineKeyboardButton(text="Back to menu", callback_data="back")]
        ]
    else:
        # Используем значения из aboutUS_button_text, а если их недостаточно, берем из default_buttons
        about_us = [
            [InlineKeyboardButton(text=aboutUS_button_text[0] if len(aboutUS_button_text) > 0 else default_buttons[0],
                                  callback_data="_",
                                  url="https://wiki.ssmu.ru/index.php?title=%D0%94%D0%BE%D0%B1%D1%80%D0%BE_%D0%BF%D0%BE%D0%B6%D0%B0%D0%BB%D0%BE%D0%B2%D0%B0%D1%82%D1%8C_%D0%B2_%D0%AD%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D0%BD%D1%83%D1%8E_%D1%8D%D0%BD%D1%86%D0%B8%D0%BA%D0%BB%BE%D0%BF%D0%B5%D0%B4%D0%B8%D1%8E_%D0%A1%D0%B8%D0%B1%D0%93%D0%9C%D0%A3")],
            [InlineKeyboardButton(text=aboutUS_button_text[1] if len(aboutUS_button_text) > 1 else default_buttons[1],
                                  callback_data="link")],
            [InlineKeyboardButton(text=aboutUS_button_text[2] if len(aboutUS_button_text) > 2 else default_buttons[2],
                                  callback_data="inst")],
            [InlineKeyboardButton(text="Back to menu", callback_data="back")]
        ]

    about_us_key = InlineKeyboardMarkup(inline_keyboard=about_us, resize_keyboard=True, one_time_keyboard=True)
    return about_us_key


def wanna_buy_key():
    storage = DataStorage()
    _, _, wannaBUY_button_text, _ = storage.get_columns()
    print("wannaBUY_button_text", wannaBUY_button_text)

    # Значения по умолчанию
    default_buttons = [
        "I am a current client",
        "I'm a new client",
        "I am a Yango client"
    ]

    if not wannaBUY_button_text:
        # Если список пустой, используем стандартные кнопки
        buy = [
            [InlineKeyboardButton(text=default_buttons[0], callback_data="old_client")],
            [InlineKeyboardButton(text=default_buttons[1], callback_data="new_client")],
            [InlineKeyboardButton(text=default_buttons[2], callback_data="client_yango")],
            [InlineKeyboardButton(text="Back to menu", callback_data="back")]
        ]
    else:
        # Используем значения из wannaBUY_button_text, а если их недостаточно, берем из default_buttons
        buy = [
            [InlineKeyboardButton(text=wannaBUY_button_text[0] if len(wannaBUY_button_text) > 0 else default_buttons[0],
                                  callback_data="old_client")],
            [InlineKeyboardButton(text=wannaBUY_button_text[1] if len(wannaBUY_button_text) > 1 else default_buttons[1],
                                  callback_data="new_client")],
            [InlineKeyboardButton(text=wannaBUY_button_text[2] if len(wannaBUY_button_text) > 2 else default_buttons[2],
                                  callback_data="client_yango")],
            [InlineKeyboardButton(text="Back to menu", callback_data="back")]
        ]

    buy_key = InlineKeyboardMarkup(inline_keyboard=buy, resize_keyboard=True, one_time_keyboard=True)
    return buy_key


def ask_keyboard():
    storage = DataStorage()
    _, _, _, goodsExpert_button_text = storage.get_columns()
    print("goodsExpert_button_text", goodsExpert_button_text)

    # Значение по умолчанию для кнопки
    default_ask_button = "Ask a question"

    if not goodsExpert_button_text:
        # Если список пустой, используем стандартные кнопки
        ask = [
            [InlineKeyboardButton(text=default_ask_button, callback_data="ask")],
            [InlineKeyboardButton(text="Back to menu", callback_data="back")]
        ]
    else:
        # Используем значение из goodsExpert_button_text, а если его нет, берем из default_ask_button
        ask = [
            [InlineKeyboardButton(
                text=goodsExpert_button_text[0] if len(goodsExpert_button_text) > 0 else default_ask_button,
                callback_data="ask")],
            [InlineKeyboardButton(text="Back to menu", callback_data="back")]
        ]

    ask_key = InlineKeyboardMarkup(inline_keyboard=ask, resize_keyboard=True, one_time_keyboard=True)
    return ask_key


back = [
    [InlineKeyboardButton(text = "Back", callback_data = "back_one_step")]
]
back_key = InlineKeyboardMarkup(inline_keyboard = back, resize_keyboard=True, one_time_keyboard=True)

admin = [
    [InlineKeyboardButton(text = "Get bot logs", callback_data = 'logs')],
    [InlineKeyboardButton(text = "Reload the keyboard", callback_data = 'reload')],
    [InlineKeyboardButton(text="Reload the texts", callback_data='texts')],
    [InlineKeyboardButton(text = "Reset hot sales", callback_data = 'reset')]
]
admin_key = InlineKeyboardMarkup(inline_keyboard = admin, resize_keyboard=True, one_time_keyboard=True)
