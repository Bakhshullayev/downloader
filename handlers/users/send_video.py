from aiogram import types
from aiogram.bot import bot
from aiogram.dispatcher.filters.builtin import CommandStart
from pytube import YouTube
from pathlib import Path
from loader import dp, bot


@dp.message_handler()
async def send_video(msg: types.Message, destination=None, mp4=None, downloads=None):
    link = msg.text
    yt = YouTube(link)
    # Showing details
    await msg.answer("Title: {}".format(str(yt.title)))
    # await msg.answer("Number of views: {}".format(str(yt.views)))
    # await msg.answer("Length of video: {}".format(str(yt.length)))
    # await msg.answer("Rating of video: {}".format(str(yt.rating)))
    # # Getting the highest resolution possible
    ys = yt.streams.get_highest_resolution()
    # Starting download
    await msg.answer("Yuklab olish jarayoni...")

    ys.download(output_path='downloads', filename='videos.mp4')
    await msg.answer("Muvaffaqiyatli yakunlandi!!")

    with open("downloads/videos.mp4","rb") as file:
        await msg.answer_video(file, caption=msg.text)
