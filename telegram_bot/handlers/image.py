from aiogram import Router, F
from aiogram.filters.text import Text
from aiogram.filters import Command
from aiogram.methods.send_message import SendMessage

from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup


from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from states.states import Menu, Text, Image
from config import bot
from generating.image.images import generate_img
router = Router()
global prompt
global num

def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

@router.message(Image.wait_prompt)
async def prompt_given(message: Message, state: FSMContext):
    global prompt
    prompt = message.text
    await state.set_state(Image.wait_num)
    await message.answer(text = 'Write number of images: ')

@router.message(Image.wait_num)
async def nums_given(message:Message, state:FSMContext):
    if(is_int(message.text)):
        await bot.send_message(chat_id = message.from_user.id, text = 'Your images: ')
        for i in range(int(message.text)):
            photo = await generate_img(prompt=prompt)
            await bot.send_photo(chat_id = message.from_user.id, photo = photo)
        await state.set_state(Menu.menu)
        await bot.send_message(chat_id = message.from_user.id, text = 'Generation ended. Use /image or /text')
    else: 
        message.answer('Write a correct number')