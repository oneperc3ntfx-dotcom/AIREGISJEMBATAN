import os

from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command


from keyboards.menu import service_menu

from utils.message import (
    WELCOME_TEXT,
    ASSISTANT_TEXT,
    COMMUNITY_TEXT,
    CHOICE_TEXT
)



router = Router()



# lokasi gambar

ASSISTANT_IMAGE = (
    "assets/ai_assistant_preview.jpg"
)


COMMUNITY_IMAGE = (
    "assets/ai_community_preview.jpg"
)





@router.message(
    Command("start")
)
async def start_handler(
    message: Message
):


    # ==========================
    # WELCOME
    # ==========================

    await message.answer(

        WELCOME_TEXT,

        parse_mode="HTML"

    )



    # ==========================
    # AI ASSISTANT IMAGE
    # ==========================

    if os.path.exists(
        ASSISTANT_IMAGE
    ):


        await message.answer_photo(

            photo=FSInputFile(
                ASSISTANT_IMAGE
            ),

            caption=ASSISTANT_TEXT,

            parse_mode="HTML"

        )


    else:


        await message.answer(

            ASSISTANT_TEXT,

            parse_mode="HTML"

        )





    # ==========================
    # COMMUNITY IMAGE
    # ==========================

    if os.path.exists(
        COMMUNITY_IMAGE
    ):


        await message.answer_photo(

            photo=FSInputFile(
                COMMUNITY_IMAGE
            ),

            caption=COMMUNITY_TEXT,

            parse_mode="HTML"

        )


    else:


        await message.answer(

            COMMUNITY_TEXT,

            parse_mode="HTML"

        )





    # ==========================
    # BUTTON MENU
    # ==========================


    await message.answer(

        CHOICE_TEXT,

        reply_markup=service_menu(),

        parse_mode="HTML"

    )
