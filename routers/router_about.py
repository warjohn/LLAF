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


router_about = Router()


@router_about.callback_query(F.data == "about_us", ALL_STATE.main)
async def main_fun(clbk: CallbackQuery, state : FSMContext):
    
    await data.delet(clbk)
    
    bot_msg = await clbk.message.answer(tt.text_about_us, reply_markup = kb.about_us_key())
    await state.set_state(ALL_STATE.about_us)
    
    
    data.msg_data.msg_id = bot_msg.message_id
