from aiogram import Router, F
from aiogram.filters.text import Text
from aiogram.filters import Command
from aiogram.methods.send_message import SendMessage

from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup


from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from states.states import Menu, Text, Image
from config import bot

router = Router()



@router.message(Command(commands=["start"]))
async def cmd_start(message: Message, state: FSMContext):
    global id
    id = str(message.from_user.id)
    #add ReadMe
    #with open('Hellomsg.txt','r') as file:
        #ans = file.read().rstrip()
    await message.answer(text='Use /image or /text')
    await state.set_state(Menu.menu)    


@router.message(Command(commands=["help"]))
async def help(message: Message):
    #with open('Help.txt','r') as file:
        #ans = file.read().rstrip()
    await message.answer(text = 'Hello! Use /image or /text')

@router.message(Command(commands=['image']))
async def date_info(message: Message, state: FSMContext):
    id = str(message.from_user.id)
    await state.set_state(Image.wait_prompt)
    await message.answer(text='Write your prompt')

@router.message(Command(commands=['text']))
async def ask_cancel_reminder(message: Message, state: FSMContext):
    await state.set_state(Text.wait_prompt)
    await message.answer(text='Write your prompt')
    

@router.message(Command(commands=['refresh']))
async def refresh(message: Message, state: FSMContext):
    await state.set_state(Menu.menu)
    await message.answer('Refreshed. Use /help to see commands')