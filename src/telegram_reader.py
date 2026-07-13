from telethon import TelegramClient
from telethon.events import NewMessage
from config import API_ID, API_HASH, PHONE, CHANNEL

client = TelegramClient("sessions/trendo", API_ID, API_HASH)


@client.on(NewMessage(chats=CHANNEL))
async def handler(event):
    print("=" * 40)
    print("NEW SIGNAL")
    print(event.raw_text)
    print("=" * 40)


async def start():
    await client.start(phone=PHONE)
    print("Telegram Connected")
    await client.run_until_disconnected()
