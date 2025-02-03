import asyncio

import aiogram.exceptions
from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile
from aiogram.types.callback_query import CallbackQuery

from aiogram.exceptions import TelegramAPIError, TelegramBadRequest
import logging
import texts.text as tt
from routers.utils.State import ALL_STATE
import keyboard.kb as kb
from routers.utils.Storage import Storage
from routers.utils.data import add_user_to_table, get_user_id, DataStorage, reset_csv, DataStorage_text
import routers.utils.data as data 



router_admin = Router()
storage = DataStorage()

@router_admin.message(Command('admin'))
async def main_fun(msg: Message, state : FSMContext):
        
    bot_msg = await msg.answer(tt.text_admin)
    await state.set_state(ALL_STATE.admin)
    
    data.msg_data.msg_id = bot_msg.message_id
    
@router_admin.message(F.text, ALL_STATE.admin)
async def verify(msg: Message, state: FSMContext):
    if str(msg.text) == '5500':
        await msg.answer(tt.text_cor_password)
        await msg.answer(tt.text_to_all, reply_markup = kb.admin_key)
        await state.set_state(ALL_STATE.all_rules)
        
    else:
        await msg.answer(tt.text_uncor_password)
        await state.clear()            
        bot_msg = await msg.answer(tt.text_start, reply_markup = kb.key_start())
        await state.set_state(ALL_STATE.main)
        
        data.msg_data.msg_id = bot_msg.message_id


@router_admin.message(F.text, ALL_STATE.all_rules)
async def add_to_bufer(msg: Message, state: FSMContext):
    try:
        data.log_message(msg.text)
        await msg.answer(tt.text_suc)

        listOFuser_id = get_user_id()
        for i in listOFuser_id:
            await msg.bot.send_message(i, msg.text)

    except TelegramAPIError:
        logging.error(f"Бот заблокирован пользователем {msg.from_user.id}")

    
@router_admin.callback_query(F.data == "logs", ALL_STATE.admin)
@router_admin.callback_query(F.data == "logs", ALL_STATE.all_rules)
async def logs(clbk: CallbackQuery, state: FSMContext):
    logs = FSInputFile('bot.log')
    await clbk.message.answer_document(logs)


@router_admin.callback_query(F.data == "reload", ALL_STATE.admin)
@router_admin.callback_query(F.data == "reload", ALL_STATE.all_rules)
async def logs(clbk: CallbackQuery, state: FSMContext):
    TABLE_NAME = "LLAF"
    SHEETS_NAME = "keyborad"
    Storage.get_button_text(TABLE_NAME, SHEETS_NAME, storage)
    print(Storage.get_button_text(TABLE_NAME, SHEETS_NAME, storage))
    await clbk.message.answer("кнопки обновленны")

@router_admin.callback_query(F.data == "texts", ALL_STATE.admin)
@router_admin.callback_query(F.data == "texts", ALL_STATE.all_rules)
async def logs(clbk: CallbackQuery, state: FSMContext):
    TABLE_NAME = "LLAF"
    SHEETS_NAME = "texts"
    storage = DataStorage_text()
    Storage.get_texts(TABLE_NAME, SHEETS_NAME, storage)
    print(Storage.get_texts(TABLE_NAME, SHEETS_NAME, storage))
    await clbk.message.answer("текста обновлены")


@router_admin.callback_query(F.data == "reset", ALL_STATE.admin)
@router_admin.callback_query(F.data == "reset", ALL_STATE.all_rules)
async def logs(clbk: CallbackQuery, state: FSMContext):
    reset_csv()
    await clbk.message.answer("Горячие предложения обновлены ")