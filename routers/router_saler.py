import asyncio

import aiogram.exceptions
from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile
from aiogram.types.callback_query import CallbackQuery

from routers.utils.Storage import Storage
from routers.utils.llm import OpenAIClient
import texts.text as tt
from routers.utils.State import ALL_STATE
import keyboard.kb as kb
from routers.utils.data import add_user_to_table
import routers.utils.data as data 


router_saler = Router()

TABLE_NAME = "LLAF"
SHEETS_NAME = "expert_of_goods"

@router_saler.message(Command("back"), ALL_STATE.saler_ask)
async def main_fun(msg: Message, state: FSMContext):
    bot_msg = await msg.answer(tt.text_saler, reply_markup=kb.ask_keyboard())
    await state.set_state(ALL_STATE.saler)

    data.msg_data.msg_id = bot_msg.message_id


@router_saler.callback_query(F.data == "saler", ALL_STATE.main)
async def main_fun(clbk: CallbackQuery, state : FSMContext):
    
    await data.delet(clbk)

    text = data.DataStorage_text()

    # Вызываем метод get_texts() на экземпляре
    _, _, saler = text.get_texts()

    print(saler)

    if not saler:
        text = tt.text_saler
    else:
        text = saler[0]

    bot_msg = await clbk.message.answer(text, reply_markup = kb.ask_keyboard())
    await state.set_state(ALL_STATE.saler)
    
    
    data.msg_data.msg_id = bot_msg.message_id
    
    
@router_saler.callback_query(F.data == "ask", ALL_STATE.saler)
async def old(clbk: CallbackQuery, state: FSMContext):
    
    await data.delet(clbk)
    
    text = "Здравтвуй"
    await clbk.message.answer(OpenAIClient.process_thread_third(text))
    await state.set_state(ALL_STATE.saler_ask)

@router_saler.message(F.text, ALL_STATE.saler_ask)
async def old_chat(msg: Message, state: FSMContext):    
    answer = OpenAIClient.process_thread_third(msg.text)
    Storage.add_data(TABLE_NAME, SHEETS_NAME, msg.from_user.id, msg.from_user.username, msg.text, answer)
    await msg.answer(text = answer)
