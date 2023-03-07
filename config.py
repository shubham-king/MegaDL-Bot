# (c) Asm Safone
# A Part of MegaDL-Bot <https://github.com/AsmSafone/MegaDL-Bot>


import os

class Config:
    API_ID = int(os.environ.get("API_ID", "16198173"))
    API_HASH = os.environ.get("API_HASH", "1298f17d50d81bb50589915ab63dbe8b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5774463474:AAFknmnzdbr8ZfWmPIh9Fl09vFAO_o85DNY")
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    TG_MAX_SIZE = 2040108421
    OWNER_ID = int(os.environ.get("OWNER_ID", 5771629925))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001649670644"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001597072284")


class TEXT:
  ABOUT = """
🤖 **Name:** {bot_name}

📝 **Language:** [Python](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted On:** [Heroku](https://t.me/RoboTez)

🧑‍💻 **Developer:** [Safone](https://t.me/Mr_RDxWap)

👥 **Support Group:** [AsmSupport](https://t.me/RoboTez)

📢 **Updates Channel:** [Ｓ１ ＢＯＴＳ](https://t.me/RoboTez)
"""

  HELP_USER = """
This is **{bot_name}**

This Bot Can Download Files & Videos From Mega Links & Upload To Telegram. Just Send Any Mega.nz Link & See The Magic. You Can Also Add or Change Caption: Just Select An Uploaded File/ Video or Forward Me Any Telegram File & Then Write The Text You Want To Be Caption On The File As A Reply To That File & The Text You Wrote Will Be Attached As Caption 😁! 

**Made With ❤️ By @RoboTez! 👑**
"""

  START_TEXT = """
👋🏻 **Hi** {user_mention},

I'm **{bot_name}**
I Can Download Files & Videos From Mega.nz Links & Upload To Telegram. Please Check Help To Learn More 😉!

**Maintained By: @RoboTez**❤️!
"""
