from telethon import events
from telethon.tl.types import MessageEntitySticker

@client.on(events.NewMessage(pattern='/id'))
async def get_premium_emoji_id(event):
    # Проверяем, есть ли это ответ на сообщение
    if event.is_reply:
        # Получаем сообщение, на которое был отправлен ответ
        reply_message = await event.get_reply_message()

        # Проверяем, содержит ли сообщение стикеры
        if reply_message.media and hasattr(reply_message.media, 'document'):
            document = reply_message.media.document
            # Ищем премиум-стикеры среди документов
            if any(attr for attr in document.attributes if isinstance(attr, MessageEntitySticker)):
                # Получаем ID стикера (или эмодзи)
                premium_emoji_id = next(attr for attr in document.attributes if isinstance(attr, MessageEntitySticker)).emoji

                # Отправляем ID эмодзи как сообщение
                await event.reply(f"ID премиум-эмодзи: {premium_emoji_id}")
            else:
                await event.reply("В сообщении нет премиум-стикеров.")
        else:
            await event.reply("Это сообщение не содержит стикеров.")
    else:
        await event.reply("Эта команда должна быть использована как ответ на сообщение со стикером.")
