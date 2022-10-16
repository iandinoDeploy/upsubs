# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from config import OWNER


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"<b>Tentang Bot ini:\n\n@{client.username} ɪɴɪ ᴀᴅᴀʟᴀʜ ʙᴏᴛ ᴘᴇɴʏɪᴍᴘᴀɴᴀɴ ᴅᴀɴ ᴘᴇɴɢɪʀɪᴍᴀɴ ᴍᴇᴅɪᴀʏᴀɴɢ ᴅɪ sʜᴀʀᴇ ᴏʟᴇʜ ᴘᴇᴍɪʟɪᴋ ᴄʜᴀɴɴᴇʟ sᴋᴀɴᴅᴀʟ ɪᴅ : @SkandalID .\n\n • ᴄʜᴀɴɴᴇʟ 1: @{OWNER}\n • ᴄʜᴀɴɴᴇʟ 2: <a href='https://t.me/RareCollectionID'>ʀᴀʀᴇ ᴄᴏʟʟᴇᴄᴛɪᴏɴ ɪᴅ</a>\n • ᴄʜᴀɴɴᴇʟ 3: @LokalPrideID \n\n💦 ғᴀᴠᴏʀɪᴛᴇ ᴄʜᴀɴɴᴇʟ @SkandalID</b>\n",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("• ᴛᴜᴛᴜᴘ •", callback_data="close")]]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
