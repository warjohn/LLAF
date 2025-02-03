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
from routers.utils.data import add_user_to_table
import routers.utils.data as data 


router_hotsales = Router()


@router_hotsales.callback_query(F.data == "hot_sales", ALL_STATE.main)
async def main_fun(clbk: CallbackQuery, state : FSMContext):
    
    await data.delet(clbk)
    
    # Получаем недавние сообщения
    admin_msg = data.get_recent_messages()
    print(admin_msg)
    if admin_msg == []:
        bot_msg = await clbk.message.answer("Администратор ещё ничего не писал :(", reply_markup=kb.back_key)
        data.msg_data.msg_id = bot_msg.message_id
        await state.set_state(ALL_STATE.hot_sales)

    # Отправляем все сообщения, кроме последнего
    for message in admin_msg[:-1]:  # Все сообщения, кроме последнего
        if message is None:
            bot_msg = await clbk.message.answer("Администратор ещё ничего не писал :(", reply_markup=kb.back_key)
            data.msg_data.msg_id = bot_msg.message_id
            await state.set_state(ALL_STATE.hot_sales)
        else:    
            await clbk.message.answer(message)
            #data.msg_data.msg_id = bot_msg.message_id
            await state.set_state(ALL_STATE.hot_sales)

    # Отправляем последнее сообщение с клавиатурой
    if admin_msg:  # Проверяем, есть ли сообщения
        bot_msg = await clbk.message.answer(admin_msg[-1], reply_markup=kb.back_key)
        data.msg_data.msg_id = bot_msg.message_id

    await state.set_state(ALL_STATE.hot_sales)
