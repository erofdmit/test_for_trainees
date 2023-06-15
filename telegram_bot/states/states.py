from aiogram import Router
from aiogram.filters.text import Text
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove





from aiogram import Router, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove


class Menu(StatesGroup):
    menu = State()


class Text(StatesGroup):
    wait_prompt = State()
    wait_creat = State()
    wait_num = State()
    wait_tok = State()

class Image(StatesGroup):
    wait_prompt = State()
    wait_num = State()