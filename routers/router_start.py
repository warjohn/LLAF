import asyncio

import aiogram.exceptions
from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile
from aiogram.types.callback_query import CallbackQuery

import texts.text as tt
from routers.utils.State import ALL_STATE
import keyboard.kb as kb
import routers.utils.data as data

router_start = Router()


@router_start.message(Command('start'))
async def main_fun(msg: Message, state : FSMContext):

    data.add_user_to_table(list(msg.from_user))
    text = data.DataStorage_text()

    # Вызываем метод get_texts() на экземпляре
    start, _, _ = text.get_texts()

    print(start)

    if not start:
        text = tt.text_start
    else:
        text = start[0]

    bot_msg = await msg.answer(text, reply_markup = kb.key_start())
    await state.set_state(ALL_STATE.main)
    
    data.msg_data.msg_id = bot_msg.message_id


@router_start.callback_query(F.data == "back_one_step", ALL_STATE.hot_sales)
@router_start.callback_query(F.data == "back", ALL_STATE.buy)
@router_start.callback_query(F.data == "back", ALL_STATE.about_us)
@router_start.callback_query(F.data == "back", ALL_STATE.saler)
async def main_fun_rt(clbk: CallbackQuery, state : FSMContext):    

    await data.delet(clbk)
    text = data.DataStorage_text()

    # Вызываем метод get_texts() на экземпляре
    start, _, _ = text.get_texts()

    print(start)

    if not start:
        text = tt.text_start
    else:
        text = start[0]

    
    bot_msg = await clbk.message.answer(text, reply_markup = kb.key_start())
    await state.set_state(ALL_STATE.main)

    data.msg_data.msg_id = bot_msg.message_id
