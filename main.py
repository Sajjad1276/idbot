# -*- coding: utf-8 -*-
"""
main.py
-------
نقطه ورود اصلی ربات. این فایل روی Railway اجرا می‌شود.
"""

import asyncio

from rubpy import Client
from rubpy.types import Update  # اگر اسمش در نسخه نصب‌شده فرق داشت، اصلاح کن

from config import SESSION_LABEL
from session_loader import ensure_session_file
from handlers import handle_message


async def run():
    session_name = ensure_session_file()
    app = Client(name=session_name)

    @app.on_message_updates()
    async def _on_message(update: Update):
        message = update.message if hasattr(update, "message") else update
        await handle_message(app, message)

    await app.start()
    print("✅ ربات با موفقیت اجرا شد و منتظر پیام‌هاست.")

    # نگه‌داشتن پروسه زنده تا وقتی سرویس متوقف نشود
    if hasattr(app, "run_until_disconnected"):
        await app.run_until_disconnected()
    else:
        while True:
            await asyncio.sleep(3600)


if __name__ == "__main__":
    asyncio.run(run())
