from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import (
    AI_ASSISTANT_URL,
    AI_COMMUNITY_URL
)



def service_menu():

    keyboard = InlineKeyboardMarkup(

        inline_keyboard=[

            [

                InlineKeyboardButton(

                    text="🤖 AI Assistant Pribadi",

                    url=AI_ASSISTANT_URL

                )

            ],

            [

                InlineKeyboardButton(

                    text="👥 AI System Analyst Community",

                    url=AI_COMMUNITY_URL

                )

            ]

        ]

    )


    return keyboard
