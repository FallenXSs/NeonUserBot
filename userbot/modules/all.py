#Neon UserBot
# CREDİT - EPİCUSERBOT
## 

from telethon.tl.types import ChannelParticipantsAdmins as cp
from userbot import CMD_HELP, bot
from userbot.events import register
from userbot.cmdhelp import CmdHelp
import asyncio

# ================================================================

@register(
	pattern="^.tag(?: |$)(.*)",
	outgoing=True, 
	groups_only=True,
)
async def tagger(q):
	if q.fwd_from:
		return

	if q.pattern_match.group(1):
		s = q.pattern_match.group(1)
	else:
		s=""
		#await q.edit("**Bir səbəb yaz...** 👀\n**Nümunə:** `.tag Aktiv olaq millət 😃🗡️`")
		return
	
	c = await q.get_input_chat()
	a_=0
	await q.delete()
	async for i in bot.iter_participants(c):
		if a_ == 5000:
			break
		a_+=1
		await q.client.send_message(q.chat_id, "**{}**\n[{}](tg://user?id={})".format(s, i.first_name, i.id))
		await asyncio.sleep(1.5)

# ======================================================================
		
@register(
	pattern="^.all(?: |$)(.*)",
	outgoing=True,
	groups_only=True,
)
async def all_tagger(q):
	if q.fwd_from:
		return

	if q.pattern_match.group(1):
		s = q.pattern_match.group(1)
	else:
		s = ""
		#await q.edit("**Bir səbəb yaz...** 👀\n**Nümunə:** `.all Salam, Necəsiz?`")
		return
	c = await q.get_input_chat()
	a_=0
	await q.delete()
	async for i in bot.iter_participants(c):
		if a_ == 5000:
			break
		a_+=1
		await q.client.send_message(q.chat_id, "**{}**\n[{}](tg://user?id={})".format(s, 
											      i.first_name, 
											      i.id)
					   						)
		await asyncio.sleep(0.5)

# -----------------------------------------------------------------

@register(
	pattern="^.alladmin(?: |$)(.*)", 
	outgoing=True,
	groups_only=True,
)
async def _(q):
	if q.fwd_from:
		return
	

	if q.pattern_match.group(1):
		s = q.pattern_match.group(1)
	else:
		s = ""
		#await q.edit("**Bir səbəb yaz...** 👀\n**Nümunə:** `.alladmin Salam, Necəsiz?`")
		return
	
	chat = await q.get_input_chat()
	a_=0
	await q.delete()
	async for i in bot.iter_participants(chat, filter=cp):
		if a_ == 50:
			break
		a_+=1
		await q.client.send_message(q.chat_id, 
					    "**{}**\n[{}](tg://user?id={})".format(s, 
											      i.first_name, 
											      i.id)
					   						)
		await sleep(1.74)
		
# ---------------------------------------------------------------------------------------------------------------
		
import re
from telethon.tl import types
from userbot import  bot

usernexp = re.compile(r"@(\w{3,32})\[(.+?)\]")
nameexp = re.compile(r"\[([\w\S]+)\]\(tg://user\?id=(\d+)\)\[(.+?)\]")


@register(
	outgoing=True, 
	ignore_unsafe=True, 
	disable_errors=True
)
async def mention(event):
    newstr = event.text
    if event.entities:
        newstr = nameexp.sub(r'<a href="tg://user?id=\2">\3</a>', newstr, 0)
        for match in usernexp.finditer(newstr):
            user = match.group(1)
            text = match.group(2)
            name, entities = await bot._parse_message_text(text, "md")
            rep = f'<a href="tg://resolve?domain={user}">{name}</a>'
            if entities:
                for e in entities:
                    tag = None
                    if isinstance(e, types.MessageEntityBold):
                        tag = "<b>{}</b>"
                    elif isinstance(e, types.MessageEntityItalic):
                        tag = "<i>{}</i>"
                    elif isinstance(e, types.MessageEntityCode):
                        tag = "<code>{}</code>"
                    elif isinstance(e, types.MessageEntityStrike):
                        tag = "<s>{}</s>"
                    elif isinstance(e, types.MessageEntityPre):
                        tag = "<pre>{}</pre>"
                    elif isinstance(e, types.MessageEntityUnderline):
                        tag = "<u>{}</u>"
                    if tag:
                        rep = tag.format(rep)
            newstr = re.sub(re.escape(match.group(0)), 
			    rep, 
			    newstr
			   )
    if newstr != event.text:
        await event.edit(newstr, 
			 parse_mode="html"
		)

# ------------------------------ CMDHELP --------------------------------------

Help = CmdHelp("tag")
Help.add_command(
	"tag", "<səbəb>", 
        "Qrupdakı şəxsləri tag edər maksimum 3.000 nəfər flood wait səbəbi ilə.")
Help.add_command(
	"all", 
        "<səbəb>", 
        "Qrupdakı şəxsləri sürətli tağ edər. Flood ola bilərsiniz.")
Help.add_command(
	"alladmin", 
        "<səbəb>", 
        "Qrupdakı adminləri tag edər")
Help.add_command(
        '@tag[istədiyiniz ad/söz]',
        'İnsanlanları istədiyiniz kimi tag edin',
        'Əvvəlində nöqtə qoymadan işlədin. Nümunə: @esebj[Qağaşşş]')  
Help.add_command(
        "restart", None, "Tag prosesini dayandırar.")
Help.add()
