from aiogram import types
from aiogram.bot import bot
from aiogram.dispatcher.filters.builtin import CommandStart
from pytube import YouTube

from loader import dp

@dp.message_handler()
async def send_video(msg:types.Message):
    link = msg.text
    yt = YouTube(link)

    # Showing details
    await msg.answer("Title: ", yt.title)
    await msg.answer("Number of views: ", "yt.views")
    await msg.answer("Length of video: ", "yt.length")
    await msg.answer("Rating of video: ", "yt.rating")
    # Getting the highest resolution possible
    ys = yt.streams.get_highest_resolution()

    # Starting download
    await msg.answer("Downloading...")
    ys.download()
    await msg.answer("Download completed!!")


