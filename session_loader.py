# -*- coding: utf-8 -*-
"""
session_loader.py
------------------
موقع استارت روی Railway (یا هر سروری)، این ماژول مقدار Environment Variable
با نام RUBIKA_SESSION را می‌خواند، base64-decode می‌کند و آن را به یک فایل
سشن واقعی (که rubpy می‌تواند مستقیم بخواندش) تبدیل می‌کند.
"""

import base64
import os

SESSION_ENV_VAR = "RUBIKA_SESSION"

# ⚠️ نکته مهم: rubpy با گرفتن یک "name" (نه مسیر کامل فایل)، خودش داخلی
# دنبال فایلی با اسم "{name}.session" در پوشه کاری فعلی (working directory)
# می‌گردد. پس باید فایل را دقیقاً با همین الگو بسازیم و به Client فقط
# همان "name" (بدون پسوند) را بدهیم.
SESSION_NAME = os.environ.get("SESSION_LABEL", "idbot_session")
SESSION_FILE_PATH = f"{SESSION_NAME}.session"


def ensure_session_file() -> str:
    """
    فایل سشن را از متغیر محیطی بازسازی می‌کند (اگر از قبل روی دیسک نبود)
    و "name"ای که باید به rubpy.Client داده شود را برمی‌گرداند
    (نه مسیر کامل فایل — چون rubpy خودش پسوند .session را اضافه می‌کند).
    """
    encoded = os.environ.get(SESSION_ENV_VAR)
    if not encoded:
        raise RuntimeError(
            f"متغیر محیطی {SESSION_ENV_VAR} تنظیم نشده است. "
            "ابتدا login.py را لوکال اجرا کن و مقدار خروجی را در Railway قرار بده."
        )

    raw = base64.b64decode(encoded)

    with open(SESSION_FILE_PATH, "wb") as f:
        f.write(raw)

    return SESSION_NAME
