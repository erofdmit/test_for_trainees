from generating.image import images
from generating.text import texts

from aiogram import Bot, types, Dispatcher
from aiogram.types import InputFile
from aiogram.filters import Command

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
import asyncio


import logging

import config
import os

from aiogram.filters import CommandObject
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import start, image, text


logging.basicConfig(level=logging.INFO)



async def on_startup(_):
    print('Online')

# Запуск бота
storage = MemoryStorage()
global dp
async def main():
    global dp
    
    bot = config.bot
    dp = Dispatcher(bot = bot, storage = storage)
    dp.include_router(start.router)
    dp.include_router(image.router)
    dp.include_router(text.router)

    
    try:
        
        await bot.delete_webhook(drop_pending_updates=True)
        await(dp.start_polling(bot))
        
        
        
    except:
        pass
    


    
if __name__ == "__main__":
    asyncio.run(main())
    
    










print('Would yout like to generate image(1) or text(2)? Print 1 or 2')
ans = int(input())
if(ans == 1):
    images.generate_img()
elif(ans == 2):
    text.generate_text()
else:
    print('Write the correct answer')