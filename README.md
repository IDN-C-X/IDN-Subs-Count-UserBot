# Subscriber Count Userbot
**A Telegram user bot to count telegram channel subscriber or group member.**

```
This tool is only for educational purpose.
You could be banned from Telegram. So be
careful.
```


## Deploying

### Deploy on [Heroku](https://heroku.com)
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/IDN-C-X/IDN-Subs-Count-UserBot)


### Local Deploy

- Clone this git repository.
```sh 
git clone https://github.com/IDN-C-X/IDN-Subs-Count-UserBot
```
- Change Directory
```sh 
cd IDN-Subs-Count-UserBot
```
- Install requirements with pip3
```sh 
pip3 install -r requirements.txt
```

### Configs (Envs)
- `BOT_TOKEN` - Get it by contacting to [BotFather](https://t.me/botfather)
- `APP_ID` - Get it by creating app on [my.telegram.org](https://my.telegram.org/apps)
- `API_HASH` - Get it by creating app on [my.telegram.org](https://my.telegram.org/apps)
- `CHANNELS` - List of channel/group usernames, seperated by space.
- `STRING_SESSION` - Pyrogram string session. run genstring.py
- `MSG_ID` - Message ID of COUNTS_EDIT_CHANNEL.
- `COUNTS_EDIT_CHANNEL` - Username of channel/group to edit the subscriber count
- `SLEEP_TIME` - Sleep time for bot before re-check the subs count, default to 10 seconds.

### Deploy 
```sh 
python3 bot.py
```

## Credit
- [Dan](https://github.com/delivrance) for [PyroGram](https://pyrogram.org)

## Copyright & License
- Copyright (©) 2021 by [IDN-C-X](https://github.com/IDN-C-X)
- Licensed under the terms of the [GNU General Public License](./LICENSE).