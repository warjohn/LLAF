import asyncio

import aiogram.exceptions
from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile
from aiogram.types.callback_query import CallbackQuery

from routers.utils.Storage import Storage
import texts.text as tt
from routers.utils.State import ALL_STATE
import keyboard.kb as kb
from routers.utils.data import add_user_to_table
import routers.utils.data as data 
from routers.utils.llm import OpenAIClient

router_buy = Router()

TABLE_NAME = "LLAF"
SHEETS_NAME = "current_client"

@router_buy.message(Command("back"), ALL_STATE.new)
@router_buy.message(Command("back"), ALL_STATE.old)
@router_buy.message(Command("back"), ALL_STATE.client_yango)
async def main_fun(msg: Message, state: FSMContext):

    bot_msg = await msg.answer(tt.text_buy, reply_markup=kb.wanna_buy_key())
    await state.set_state(ALL_STATE.buy)

    data.msg_data.msg_id = bot_msg.message_id

@router_buy.callback_query(F.data == "buy", ALL_STATE.main)
async def main_fun(clbk: CallbackQuery, state : FSMContext):
    
    await data.delet(clbk)
    text = data.DataStorage_text()

    # Вызываем метод get_texts() на экземпляре
    _, buy, _ = text.get_texts()

    print(buy)

    if not buy:
        text = tt.text_buy
    else:
        text = buy[0]

    bot_msg = await clbk.message.answer(text, reply_markup = kb.wanna_buy_key())
    await state.set_state(ALL_STATE.buy)
    
    
    data.msg_data.msg_id = bot_msg.message_id


@router_buy.callback_query(F.data == "old_client", ALL_STATE.buy)
async def old(clbk: CallbackQuery, state: FSMContext):
    
    await data.delet(clbk)
    
    text = "Здравствуй"
    await clbk.message.answer(OpenAIClient.process_thread(text, 1))
    await state.set_state(ALL_STATE.old)

@router_buy.message(F.text, ALL_STATE.old)
async def old_chat(msg: Message, state: FSMContext):

    answer = OpenAIClient.process_thread(msg.text, 1)
    Storage.add_data(TABLE_NAME, SHEETS_NAME, msg.from_user.id, msg.from_user.username, msg.text, answer)
    await msg.answer(answer)
    

@router_buy.callback_query(F.data == "new_client", ALL_STATE.buy)
async def new(clbk: CallbackQuery, state: FSMContext):
    
    await data.delet(clbk)
    
    text = "Здравствуй"
    await clbk.message.answer(OpenAIClient.process_thread(text, 2))
    await state.set_state(ALL_STATE.new)
    
@router_buy.message(F.text, ALL_STATE.new)
async def new_chat(msg: Message, state: FSMContext):

    answer = OpenAIClient.process_thread(msg.text, 2)
    Storage.add_data(TABLE_NAME, 'new_client', msg.from_user.id, msg.from_user.username, msg.text, answer)
    await msg.answer(text = answer)
    
    
@router_buy.callback_query(F.data == "client_yango", ALL_STATE.buy)
async def old(clbk: CallbackQuery, state: FSMContext):
    
    await data.delet(clbk)
    
    text = "Здравствуй"
    await clbk.message.answer(OpenAIClient.process_thread(text, 0))
    await state.set_state(ALL_STATE.client_yango)

@router_buy.message(F.text, ALL_STATE.client_yango)
async def old_chat(msg: Message, state: FSMContext):

    answer = OpenAIClient.process_thread(msg.text, 0)
    Storage.add_data(TABLE_NAME, "yango_client", msg.from_user.id, msg.from_user.username, msg.text, answer)
    await msg.answer(answer)
