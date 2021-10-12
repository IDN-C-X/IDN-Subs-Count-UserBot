import asyncio, os, requests, json
from pyrogram import Client
from pyrogram.errors import FloodWait

API_HASH = os.environ['API_HASH']
APP_ID = int(os.environ['APP_ID'])
CHANNELS = os.environ['CHANNELS']
STRING_SESSION = os.environ['STRING_SESSION']

CHANNELS = [i for i in CHANNELS.split(' ')]
MSG_ID = int(os.environ['MSG_ID'])
COUNTS_EDIT_CHANNEL = os.environ['COUNTS_EDIT_CHANNEL']

# Running bot
xbot = Client(api_id=APP_ID, api_hash=API_HASH, session_name=STRING_SESSION)

# Helper
def getdicks(channel):
  url = f'https://tglivesubsapi.vercel.app/getsubs/{channel}'
  x = json.loads(requests.get(url).text)
  return x['subs'], x['channel_name']

# Main script
async def runbot():
  async with xbot:
    while True:
      print("Checking")
      toprint = '**Subsriber Count**\n\n'
      for channel in CHANNELS:
        ch = getdicks(channel)
        CH_TITLE =  ch[1]
        CH_MCOUNT = str('{0:,}'.format(int(ch[0])))
        CH_USERNAME = channel
        toprint += f'<a href=https://t.me/{CH_USERNAME}>{CH_TITLE}</a>: `{CH_MCOUNT}`\n'
      me = await xbot.get_me()
      toprint += f'\nBy <a href=tg://user?id={str(me.id)}>{me.first_name}</a>'
      f = await xbot.get_messages(COUNTS_EDIT_CHANNEL, MSG_ID)
      if f.text.html == toprint:
        print('Checked')
      else:
        try:
          await xbot.edit_message_text(COUNTS_EDIT_CHANNEL, MSG_ID, toprint, disable_web_page_preview=True)
        except FloodWait as e:
          print(f'FloodWait: Sleeping for {str(e.x)} seconds')
          await asyncio.sleep(e.x)
          pass
        print('Checked')

xbot.run(runbot())