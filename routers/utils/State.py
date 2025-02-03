from aiogram.fsm.state import State, StatesGroup

class ALL_STATE(StatesGroup):
    main = State()
    about_us = State()
    buy = State()
    old = State()
    new = State()
    saler = State()
    saler_ask = State()
    admin = State()
    all_rules = State()
    hot_sales = State()
    client_yango = State()