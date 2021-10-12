from pyrogram import Client

api_id = input("Enter Your APP ID: ")
api_hash = input("Enter Your API HASH: ")

with Client("IDN-Coder-X", api_id=int(api_id), api_hash=api_hash) as xbot:
  ssession = f'**String Session**:\n`{xbot.export_session_string()}`'
  xbot.send_message('me', ssession)
  print('Your string session has been stored to your saved message')