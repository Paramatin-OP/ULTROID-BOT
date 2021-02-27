"""
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))

                 MADE BY LEGENDX22
                 IDEA BY PROBOY22
                 CREDITS TEAMLEGEND
                 PLEASE KEEP CREDITS 🥺
"""



from LEGEND import admin_cmd


@bot.on(admin_cmd(outgoing=True, pattern="hehe"))
async def repo(event):
    if event.fwd_from:
        return
    LEGENDX = Var.BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(LEGENDX, "hehe")
    await response[0].click(event.chat_id)
    await event.delete()


"""
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
"""



BOT = "ULTROID"
from telethon import events, Button, custom
import os,re
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
@tgbot.on(events.InlineQuery(pattern=r"hehe"))
async def inline_id_handler(event: events.InlineQuery.Event):
 LEGEND = event.builder
 X= [[custom.Button.inline("🔥 REPO🔥",data="PROBOY"), custom.Button.inline("😎ALL REPOS😎", data="LEGENDX")]]
 query = event.text
 result = LEGEND.article("LEGEND",text="REPO AND SUPPORT",buttons=X,link_preview=False)
 await event.answer([result])
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"PROBOY")))
async def callback_query_handler(event):

# inline by LEGENDX22 and PROBOY22 🔥
  await event.edit(text=f"{BOT} REPO AND GROUP LINK",buttons=[[Button.url(f"🔥{BOT} REPO🔥", url="http://github.com/ULTROID-OP/ULTROID-BOT"), Button.url(f"⚡️{BOT} SUPPORT⚡️", url="https://t.me/ULTROID_OP")]])


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"LEGENDX")))
async def callback_query_handler(event):
# inline by LEGENDX22 and PROBOY22 🔥
  PROBOYX = [[Button.url("REPO-LEGEND", url="https://gitHub.com/LEGENDXOP/LEGEND-BOT"), Button.url("REPO-ULTROID X", url="https://gitHub.com/ULTROID-OP/ULTROID-BOT"), Button.url("DEPLOY-LEGENX", url="https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Flegendxop%2Flegend-bot&template=https%3A%2F%2Fgithub.com%2FLEGENDXOP%2FLEGEND-BOT"), Button.url("DEPPLOY-ULTROID", url="https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FULTROID-OP%2FULTROID-BOT&template=https%3A%2F%2Fgithub.com%2FULTROID-OP%2FULTROID-BOT", Button.url("TUTORIAL", url="https://youtu.be/rGCSSFPsS4Q"), Button.url("STRING-SESSION", url="https://repl.it/@legendx22/LEGEND-BOT#main.py"), Button.url("API_ID & HASH", url="https://t.me/usetgxbot"), Button.url("REDIS", url="https://redislabs.com), Button.url("SUPPORT GROUP", url="https://t.me/LEGENDBOT_OFFICIAL"), Button.url("SUPPORT GROUP", url="https://t.me/LEGEND_USERBOT_SUPPORT"), Button.switch_inline("RE SEARCH", query="hehe", same_peer=True)]]
  await event.edit(text=f"ALL DETAILS OF REPOS",buttons=PROBOYX)