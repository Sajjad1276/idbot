# -*- coding: utf-8 -*-
"""
userinfo.py
-----------
گرفتن اطلاعات یک کاربر از روی guid و ساخت متن فارسی خروجی
(بدون بخش تاریخ ثبت‌نام — طبق تصمیم پروژه حذف شده است).
"""


async def get_user_info(bot, guid: str) -> dict:
    """
    دریافت اطلاعات یک کاربر/چت از روی guid.

    ⚠️ نام دقیق این متد در rubpy باید تأیید شود. نامزدهای محتمل:
        - bot.get_object_info(guid)
        - bot.getObjectInfo(guid)
    اگر اجرا خطای AttributeError داد، در مستندات docs.rubpy.site
    اسم درست را پیدا کن و همین یک خط را جایگزین کن.
    """
    info = await bot.get_object_info(guid)
    return info


def build_info_message(guid: str, info: dict, title: str = "مشخصات کاربر") -> str:
    """
    ساخت متن فارسی خروجی مشابه فرمت IDbot در تلگرام (بدون تاریخ ثبت‌نام).
    """
    first_name = (info or {}).get("first_name", "") or ""
    last_name = (info or {}).get("last_name", "") or ""
    full_name = f"{first_name} {last_name}".strip() or "—"

    username = (info or {}).get("username")
    username_display = f"@{username}" if username else "ندارد"

    lines = [
        f"👤 {title}",
        "",
        f"🆔 شناسه: {guid}",
        f"🔗 نام کاربری: {username_display}",
        f"📝 نام: {full_name}",
    ]
    return "\n".join(lines)
