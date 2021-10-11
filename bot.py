import asyncio, os
from pyrogram import Client
from pyrogram.errors import FloodWait, BadRequest

API_HASH = os.environ['API_HASH']
APP_ID = int(os.environ['APP_ID'])
CHANNELS = os.environ['CHANNELS']
STRING_SESSION = os.environ['STRING_SESSION']

CHANNELS = [i for i in CHANNELS.split(' ')]
MSG_ID = int(os.environ['MSG_ID'])
COUNTS_EDIT_CHANNEL = os.environ['COUNTS_EDIT_CHANNEL']
SLEEP_TIME = int(os.environ['SLEEP_TIME'])

# Running bot
xbot = Client(api_id=APP_ID, api_hash=API_HASH, session_name=STRING_SESSION)

# Main script
async def runbot():
  async with xbot:
    while True:
      print("Checking")
      toprint = '**Subsriber Count**\n\n'
      for channel in CHANNELS:
        ch = await xbot.get_chat(channel)
        CH_TITLE =  ch.title
        CH_MCOUNT = ch.members_count
        CH_USERNAME = ch.username
        toprint += f'<a href=https://t.me/{CH_USERNAME}>{CH_TITLE}</a>: {CH_MCOUNT}\n'
      me = await xbot.get_me()
      toprint += f'\nBy <a href=tg://user?id={str(me.id)}>{me.first_name}</a>'
      try:
        await xbot.edit_message_text(COUNTS_EDIT_CHANNEL, MSG_ID, toprint, disable_web_page_preview=True)
      except FloodWait as e:
        print(f'Floodwait: {e.x}')
        await asyncio.sleep(e.x)
        pass
      except BadRequest:
        pass
      print(f'Sleeping for {SLEEP_TIME} seconds')
      print('Checked')
      await asyncio.sleep(SLEEP_TIME)

xbot.run(runbot())