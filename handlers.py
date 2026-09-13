# -*- coding: utf-8 -*-
"""
handlers.py
-----------
منطق دو حالت اصلی ربات:
    1) دیدن دستور /start در پیوی -> نمایش مشخصات خود فرستنده
    2) دیدن پیام فوروارد شده (هرجا) -> نمایش مشخصات فرستنده اصلی پیام
"""

from userinfo import build_info_message, get_user_info


def extract_forwarded_guid(message: dict):
    """
    تلاش برای استخراج guid فرستنده اصلی از یک پیام فوروارد شده.

    ⚠️ ساختار دقیق کلیدها باید با تست واقعی روی یک پیام فوروارد شده
    تأیید شود. برای دیباگ، یک بار کل دیکشنری message را چاپ کن و ببین
    کلید مربوط به فوروارد دقیقاً چه اسمی دارد و guid کجای آن است.
    نامزدهای محتمل: forwarded_from / forward_from
    """
    forwarded = message.get("forwarded_from") or message.get("forward_from")
    if not forwarded:
        return None
    return forwarded.get("object_guid") or forwarded.get("user_guid")


async def handle_message(bot, message: dict):
    """
    تابع اصلی که برای هر پیام دریافتی صدا زده می‌شود.
    """
    chat_guid = message.get("object_guid")
    sender_guid = message.get("author_object_guid") or message.get("author_guid")
    text = (message.get("text") or "").strip()

    # حالت ۱: دستور /start
    if text == "/start":
        info = await get_user_info(bot, sender_guid)
        reply = build_info_message(sender_guid, info, title="مشخصات شما")
        await bot.send_text(chat_guid, reply)
        return

    # حالت ۲: پیام فوروارد شده
    fwd_guid = extract_forwarded_guid(message)
    if fwd_guid:
        info = await get_user_info(bot, fwd_guid)
        reply = build_info_message(fwd_guid, info, title="مشخصات فرد فوروارد شده")
        await bot.send_text(chat_guid, reply)
        return
